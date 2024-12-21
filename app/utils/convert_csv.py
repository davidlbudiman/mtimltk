import pandas
import pandas as pd
import sqlite3
import os
import pandas as pd
import plotly.express as px


def read_csv(filepath='../../data/RAW_interactions.csv'):
    df = pd.read_csv(filepath)
    return df


def connect_to_sqlite_db(database='../storage/database.db'):
    conn = sqlite3.connect(database)
    return conn, conn.cursor()


def create_table(cursor: sqlite3.Cursor, table_definition='CREATE TABLE IF NOT EXISTS interactions_raw(user_id INT, recipe_id INT, date DATETIME, rating DOUBLE, review TEXT);'):
    cursor.execute(table_definition)


def insert_into_table(df: pandas.DataFrame, conn: sqlite3.Connection, table='interactions_raw', if_exists='fail'):
    df.to_sql(table, conn, if_exists, index=False)

