import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="07010107lynnGKGK!",
    database="testdatabase"
)

mycursor = db.cursor()

# # list the name of the columns in the brackets
# # TYPE is variable characters means string up to the length 50
# # UNSIGNED: no negative numbers
# # PRIMARY KEY: unique value associate with each row
# # everytime you add an entry in, this key will be generated and will be different
# mycursor.execute("CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")

# #plot this table
# mycursor.execute("DESCRIBE Person")


# # add elements
mycursor.execute("INSERT INTO Person (name, age) VALUES (%s, %s)", ("Joe", 22))
# # database commit changes, it will commit those changes and those will actually be saved permanently
db.commit()  # 每次增加items都运行，与INSERT一起运行

# # give me all the output that my cursor got from this SQL query
# for x in mycursor:
#     print(x)

# get all of the rows and all of the items that are inside of our database
# Select everything from the table Person and give it to us
mycursor.execute("SELECT * FROM Person")
for x in mycursor:
    print(x)
