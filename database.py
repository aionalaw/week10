import sqlite3 as sql

conn = sqlite3.connect('database.db')
print("opened database successfully")

conn.exceute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
print("Table created successfully")

conn.close()