import os
import pymysql

# Get username from Cloud9 workspace
# Modify this variable if running in another environment

username = os.getenv('C9-USER')

# Connect to the database
connection = pymysql.connect(
    host='localhost', user=username, password='', db='Chinook')

try:
    # run a query
    with connection.cursor() as cursor:
        sql: "SELECT * from Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
    
finally:
    # Close the connection, regardless of whether the above was successful.
    connection.close()
