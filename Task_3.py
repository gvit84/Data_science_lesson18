import mysql.connector

#Task_3
# Create Connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123454321",
    database="my_first_db"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS employee (id INT AUTO_INCREMENT PRIMARY KEY, "
                 "name VARCHAR(255), salary INT(6))")
