# foreign keys is to allow you to reference one table from another.
# One column in the child table is gonna be the same as the colum in the parent table.
# This column can be called as a foreign key.
# foreign keys don't necessary need to be unique. e.g. one user can have many post on FB.

import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="07010107lynnGKGK!",
    database="testdatabase"
)

users = [("tim", "techwithtim"),
         ("joe", "joey123"),
         ("sarah", "sarah1234")]

user_scores = [(45, 100),
               (30, 200),
               (46, 124)]

mycursor = db.cursor()

# Create the user table
Q1 = "CREATE TABLE Users (id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), passwd VARCHAR (50))"

Q2 = "CREATE TABLE Scores (userId int PRIMARY KEY, FOREIGN KEY(userId) REFERENCES Users(id), game1 int DEFAULT 0, game2 int DEFAULT 0)"

# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#     print(x)

# # WAY ONE: add users
# # take all users (tuples) and it's gonna run the queries three times
# mycursor.executemany("INSERT INTO Users (name, passwd) VALUES (%s,%s)", users)

# WAY TWO:
Q3 = "INSERT INTO Users (name, passwd) VALUES (%s,%s)"
Q4 = "INSERT INTO Scores (userID, game1, game2) VALUES (%s,%s,%s)"

for x, user in enumerate(users):
    mycursor.execute(Q3, user)
    last_id = mycursor.lastrowid  # get the last row ID that was inserted into the table
    # it's gonna to be the ID of the user that we insert in because it's getting the primary key of the entries we
    # put in.
    mycursor.execute(Q4, (last_id,) + user_scores[x])
    # creating tuples (id, game1, game2) + usercores corresponding to users
db.commit()

mycursor.execute("SELECT * FROM Scores")
for x in mycursor:
    print(x)

mycursor.execute("SELECT * FROM Users")
for x in mycursor:
    print(x)