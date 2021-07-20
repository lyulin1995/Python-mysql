import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="07010107lynnGKGK!",
    database="testdatabase"
)

mycursor = db.cursor()

