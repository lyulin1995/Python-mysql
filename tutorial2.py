import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="07010107lynnGKGK!",
    database="testdatabase"
)

mycursor = db.cursor()

# # ENUM allows you to select between a few different values
# # datetime is a Python datetime object
# mycursor.execute("CREATE TABLE Test (name varchar(50) NOT NULL, created datetime NOT NULL, gender ENUM('M', 'F', 'O') NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT)")

###### Selecting
# mycursor.execute("INSERT INTO Test (name, created, gender) VALUES (%s,%s,%s)", ("Joey", datetime.now(), 'F'))
# db.commit()
# mycursor.execute("SELECT id, name FROM Test WHERE gender = 'M' ORDER BY id DESC")
# for x in mycursor:
#     print(x)

###### Modify a table
# # add a column
# mycursor.execute("ALTER TABLE Test ADD COLUMN food varchar(50) NOT NULL")
# mycursor.execute("DESCRIBE Test")
# # return the first entry by mu cursor
# print(mycursor.fetchone())

# # remove a column
# mycursor.execute("ALTER TABLE Test DROP food")

# # change a column name: name -> first_name, and type
mycursor.execute("ALTER TABLE Test CHANGE name first_name VARCHAR(50)")

# show all of them
mycursor.execute("DESCRIBE Test")
for x in mycursor:
    print(x)