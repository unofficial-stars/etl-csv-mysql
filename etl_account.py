import pymysql
import petl as etl
import pandas as pd
import sys, os
import pathlib
import psycopg2


def main():
    workdir = pathlib.Path(__file__).absolute()

    conn_myptm = pymysql.connect(
        host="CONTABO_UNOFFICIAL",
        user="EKO",
        password="EKO",
        database="data_information_platform",
        port=3306,
        connect_timeout=50,
    )

    # path = workdir.parent.joinpath("sql/extract_prev_30_n_today.sql")
    # query = open(path, "r").read()
    table = etl.fromdb(conn_myptm, "select * from account")
    print(table)
    df = etl.todataframe(table)
    print(df)
    # df["created_at"] = pd.to_datetime(df.created_at, format="%Y%m%d%H%M%S")
    df["created_at"] = df["created_at"].apply(
        lambda x: pd.Timestamp(x).strftime("%Y-%m-%d %H:%M:%S")
    )

    # df["updated_at"] = pd.to_datetime(df.updated_at, format="%Y%m%d%H%M%S")
    df["updated_at"] = df["updated_at"].apply(
        lambda x: pd.Timestamp(x).strftime("%Y-%m-%d %H:%M:%S")
    )

    conn_myptm.close()

    conn_dwh = psycopg2.connect(
        host="postgres",
        user="EKO",
        password="EKO",
        database="unofficial_dwh",
        port=5432,
        connect_timeout=50,
    )

    # conn_dwh.cursor().execute('SET SQL_MODE=ANSI_QUOTES')

    table = etl.fromdataframe(df)

    etl.todb(table, conn_dwh, "testing_dbt_account", create=True)
    conn_dwh.close()


if __name__ == "__main__":
    main()


# --> etl fromdb
# --> etl todb  ( create = true )
