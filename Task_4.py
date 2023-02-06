import mysql.connector

#Task_4
# Create Connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123454321",
    database="my_first_db"
)

mycursor = mydb.cursor()
mycursor.execute("ALTER TABLE student CHANGE COLUMN id PRIMARY_KEY INT")
