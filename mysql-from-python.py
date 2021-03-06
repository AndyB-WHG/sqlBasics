import os
import datetime
import pymysql

# Get username from Cloud9 workspace
# (modify this variable if running on another environment)
username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:
        # cursor.execute(""" CREATE TABLE IF NOT EXISTS
        #                 Friends(name char(20), age int, DOB datetime);""")
        rows = cursor.executemany("Delete from Friends where name = %s;",
                              ['Bob', 'Simon', 'Gemma'])
        connection.commit()

finally:
    # Close the connection, regardless of whether or not the above was successful.
    connection.close()
