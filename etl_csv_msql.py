import pymysql
import petl as etl
import pandas as pd
import sys, os
import pathlib
import psycopg2


def main():

    # read csv pandas
    
    workdir = pathlib.Path(__file__).absolute()

    path = workdir.parent.joinpath("salaries.csv")

    datas = pd.read_csv(path)

    print(datas)

    conn_mysql = pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="testing",
        port=3306,
        connect_timeout=50,
    )

    table = etl.fromdataframe(datas)
    
    print(table)

    conn_mysql.cursor().execute('SET SQL_MODE=ANSI_QUOTES')

    etl.todb(table, conn_mysql, "data_salaries", create=True)
    conn_mysql.close()


if __name__ == "__main__":
    main()


# --> etl fromdb
# --> etl todb  ( create = true )
