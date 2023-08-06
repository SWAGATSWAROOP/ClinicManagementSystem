import pandas as pd
import mysql.connector as mysql
from mysql.connector import Error


connection = mysql.connect(
  host="localhost",
  user="sqluser",
  password="password",
  database="Mamu"
)

def create_database(query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")

print(connection)

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")
        

