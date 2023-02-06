import mysql.connector

#Task_5
# Create Connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123454321",
    database="my_first_db"
)

mycursor = mydb.cursor()
sql = "INSERT INTO student (id, name) VALUES (%s, %s)"
val = (1, "john")
mycursor.execute(sql, val)

sql2 = "INSERT INTO employee (id, name, salary) VALUES (%s, %s, %s)"
val2 = (1, "john", 10000)
mycursor.execute(sql2, val2)

mydb.commit()
