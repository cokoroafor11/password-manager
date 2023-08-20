import psycopg2
from config import *


def create_table(table_name):
    """ create table in the PostgreSQL database"""
    sql = (
        """
        CREATE TABLE {} (
            username VARCHAR (256) NOT NULL,
            password VARCHAR (256) NOT NULL,
            email VARCHAR (320) NOT NULL,
            app_name TEXT NOT NULL,
            website TEXT NOT NULL
            )
            """.format(str(table_name)))
    conn = None
    try:
        #establishing the connection
        conn = psycopg2.connect(
        database=database, user=user, password=password, host=host, port= port
        )
        conn.autocommit = True
        #Creating a cursor object using the cursor() method
        cursor = conn.cursor()
        #Creating a table
        cursor.execute(sql)
        print("Table created successfully........")

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def delete_table(table_name):
    """create table in the PostgreSQL databaset"""
    sql = (
        """
        DROP TABLE {}
        """.format(str(table_name))
    )

    conn = None
    try:
        #establishing the connection
        conn = psycopg2.connect(
        database=database, user=user, password=password, host=host, port= port
        )
        conn.autocommit = True
        #Creating a cursor object using the cursor() method
        cursor = conn.cursor()
        #Creating a table
        cursor.execute(sql)
        print("Table created successfully........")

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    table_name = input('Please input your table name: ')
    create_table(table_name)