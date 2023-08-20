

import psycopg2
from config import *

def create_database(db_name):
    #establishing the connection
    conn = psycopg2.connect(
    database=database, user=user, password=password, host=host, port= port
    )
    conn.autocommit = True

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    #Preparing query to create a database
    sql = '''CREATE database {}'''.format(str(db_name))

    #Creating a database
    cursor.execute(sql)
    print("Database created successfully........")

    #Closing the connection
    conn.close()

if __name__ == '__main__':
    create_database(db_name)