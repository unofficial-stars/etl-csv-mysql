import pymysql
import petl as etl
import pandas as pd
import pathlib
import sys


def main(input_file, db_host, db_name, table_output_name):
    # read csv pandas
    workdir = pathlib.Path(__file__).absolute()
    path = workdir.parent.joinpath(input_file)
    datas = pd.read_csv(path)

    print(datas)

    conn_mysql = pymysql.connect(
        host=db_host,
        user="root",
        password="root",
        database=db_name,
        port=3306,
        connect_timeout=50,
    )

    table = etl.fromdataframe(datas)

    print(table)

    conn_mysql.cursor().execute("SET SQL_MODE=ANSI_QUOTES")

    etl.todb(table, conn_mysql, table_output_name, create=True)
    conn_mysql.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python etl_csv_msql.py input.csv db_host db_name table_name")
    else:
        input_csv = pathlib.Path(sys.argv[1])
        db_host = pathlib.Path(sys.argv[2])
        db_name = pathlib.Path(sys.argv[3])
        table_output_name = pathlib.Path(sys.argv[4])
        main(input_csv, str(db_host), str(db_name), str(table_output_name))

# python etl_csv_msql.py Traffic.csv mysql testing traffic
# --> etl fromdb
# --> etl todb  ( create = true )
