# Password Manager

Password Manager is an application run through the command line that allows you to store passwords for various accounts in one place. Additionally, the application can generate unique passwords for you to use and store.

## Installation
Download [PostgresQL](https://www.postgresql.org/download/) from the website if you haven't done so already.

Additionally, you can install [pgAdmin](https://www.pgadmin.org/download/) for database management and visualization.

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install psycopg2, which is a Postgres database adapter for Python.
```bash
python -m pip install psycopg2
```

## Setup
Run create_db.py script to create the actual PostgreSQL database. Record the database name you choose as well as the credentials used to later access the database as needed. You will need all of these for a config.py file that cotains info for connection to db:
```python
db_name = #name you chose during setup
database = #usually just 'postgres'
user = #usually just 'postgres'
password = #password you chose during setup
host = #Usually local: 127.0.0.1
port = #Usually 5432
```

## Usage
The application is run through the password_manager.py file, which provides you with the following tasks that you may perform.

```
Welcome to password manager. What would you like to do?
 1: Retrieve password
 2: Add password
 3: Delete password
 4: Update password
 5: Generate password
 6: View table
 7: Create table
 8: Delete table
 0: Exit
```

## Notes
The name for the table you create needs to be "passwords" as this is what is used for all queries. You can change this, but it would mean you need to update all SQL queries with the appropriate database name

## Next Steps
1. Need to build in encryption for passwords so they aren't stored as plaintext in the database
2. Will potentially implement a GUI in tkinter if it improves ease of use.
