import os
import pyodbc
import pandas as pd


def odbc_url():
    drill_odbc_url = os.getenv('DRILL_ODBC_URL',
                               'Driver=/opt/mapr/drill/lib/64/libdrillodbc_sb64.so;AuthenticationType=No Authentication;ConnectionType=ZooKeeper;ZKQuorum=zookeeper:2181;ZKClusterID=drillbits1;')
    return drill_odbc_url


def connect(url=None):
    if url is None:
        url = odbc_url()
    return pyodbc.connect(url, autocommit=True)


def read_sql(
    sql='select 1',
    index_col=None,
    coerce_float=True,
    params=None,
    parse_dates=None,
    columns=None,
    chunksize=None
):
    conn = connect()
    return pd.read_sql(sql, conn, index_col, coerce_float, params, parse_dates, columns, chunksize)


def read_table(
    table,
    index_col=None,
    coerce_float=True,
    params=None,
    parse_dates=None,
    columns=None,
    chunksize=None
):
    sql = 'select * from ' + table
    return read_sql(sql, index_col, coerce_float, params, parse_dates, columns, chunksize)
