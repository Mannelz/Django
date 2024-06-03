# Install Mysql on your computer
# https://dev.mysql.com/downloads/installer/
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python 

import pymysql

dataBase = pymysql.connect(
	host = 'localhost',
	user = 'root',
	passwd = '12345'

	)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE mannelz")

print("All Done!")