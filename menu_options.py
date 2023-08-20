#Menu
#Options
## Create database
## Add password (with website and username)
## Remove password
## Change Password
## Retrieve password
## Option to autogenerate password
##

##Require database password
##Copy passwords to clipboard
##Recurring auto-updates?
import psycopg2
from psycopg2 import sql
import pandas as pd
import string
import secrets
from config import *
import warnings


letters = string.ascii_letters
digits = string.digits
special = string.punctuation
alpha = letters+digits+special


def add_pass(app_user,app_pw,app_email,app_name,app_website):
    args = [app_user,app_pw,app_email,app_name,app_website]
    args = [elem.strip().lower() for elem in args]

    try:
        #establishing the connection
        conn = psycopg2.connect(
        database=database, user=user, password=password, host=host, port=port
        )
        conn.autocommit = True
        #Creating a cursor object using the cursor() method
        cursor = conn.cursor()
        #Preparing query to create a database
        insert_query = """ INSERT INTO passwords (username, password, email, app_name, website) 
                            VALUES (%s, %s, %s, %s, %s) """
        
        record = (args[0],args[1],args[2],args[3],args[4])
        cursor.execute(insert_query, record)

        print("\nRecord inserted successfully...\n")

        #Closing the connection
        conn.close()
    except (Exception, psycopg2.Error) as error:
        print(error)

def retrieve_pass(username,app_name):
    app_name = app_name.strip().lower()
    try:
        #establishing the connection
        conn = psycopg2.connect(
        database=database, user=user, password=password, host=host, port= port
        )
        conn.autocommit = True
        #Creating a cursor object using the cursor() method
        cursor = conn.cursor()
        #Preparing query to create a database
        retrieve_query = """SELECT password from passwords WHERE app_name = %(value1)s and username = %(value2)s """
        record = ({"value1": app_name, "value2": username})
        cursor.execute(retrieve_query,record)
        retrieved_pass = cursor.fetchone()

        print("\nThe password for this site is: {}\n".format(retrieved_pass))

        #Closing the connection
        conn.close()
    except (Exception, psycopg2.Error) as error:
        print(error)

def delete_pass(username,app_name):
    try:
        #establishing the connection
        conn = psycopg2.connect(
        database=database, user=user, password=password, host=host, port= port
        )
        conn.autocommit = True
        #Creating a cursor object using the cursor() method
        cursor = conn.cursor()
        #Preparing query to create a database
        delete_query = """DELETE FROM passwords WHERE app_name = %s and username = %s"""
        record = (app_name,username)
        cursor.execute(delete_query,record)
        #retrieved_pass = cursor.fetchone()

        print("This entry has been deleted!\n")

        #Closing the connection
        conn.close()
    except (Exception, psycopg2.Error) as error:
        print(error)

def update_pass(username,app_name,new_pass):
    try:
        #establishing the connection
        conn = psycopg2.connect(
        database=database, user=user, password=password, host=host, port= port
        )
        conn.autocommit = True
        #Creating a cursor object using the cursor() method
        cursor = conn.cursor()
        #Preparing query to create a database
        update_query = """UPDATE passwords SET password = %s WHERE app_name = %s and username = %s"""
        record = (new_pass,app_name,username)
        cursor.execute(update_query,record)

        print("This entry has been updated!\n")

        #Closing the connection
        conn.close()
    except (Exception, psycopg2.Error) as error:
        print(error)

def generate_pass(length):
    while True:
        pwd = ''
        for i in range(length):
            pwd += ''.join(secrets.choice(alpha))
        if (any(char in special for char in pwd) and \
            sum(dig in digits for dig in pwd)>=1 and \
            sum(char in alpha for char in pwd)>1):
          break
    return pwd

def view_database(db_name):
    
    try:
        #establishing the connection
        conn = psycopg2.connect(
        database=database, user=user, password=password, host=host, port= port
        )
        conn.autocommit = True
        #Creating a cursor object using the cursor() method
        cursor = conn.cursor()
        
        warnings.filterwarnings("ignore", category=UserWarning)
        my_table = pd.read_sql('''select * from {}'''.format(db_name), conn)
        #my_table = pd.read_sql('''select * from passwords''', conn)
        print(my_table)
        print('\n')
        #Closing the connection
        conn.close()
    except (Exception, psycopg2.Error) as error:
        print(error)

arr = ['hello','what','hello@yahoo.com','yahoo','yahoo.com']
#add_pass(arr[0],arr[1],arr[2],arr[3],arr[4])
#retrieve_pass('yahoo','yooo')
#delete_pass('hello','yahoo')
#update_pass('goat_james','gmail','howsitgoing')
view_database('passwords')

