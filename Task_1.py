import mysql.connector

#Task_1
# Create Connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123454321"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS my_first_db")
