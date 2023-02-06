import mysql.connector

#Task_2
# Create Connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123454321",
    database="my_first_db"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS student (id INT, name VARCHAR(255))")
