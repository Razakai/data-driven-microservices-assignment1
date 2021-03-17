#from databases import Database
from database.const import DB_USER, DB_HOST, DB_NAME, DB_PASSWORD
import mysql.connector

def getDB():
    return mysql.connector.connect(
            host = DB_HOST,
            user = DB_USER,
            password = DB_PASSWORD,
            database = DB_NAME
    )

def fetch(query) -> list:  # get
    try:
        db = getDB()
        mycursor = db.cursor()
        mycursor.execute(query)
        res = mycursor.fetchall()
        mycursor.close()
        db.close()
        return res
        

    except Exception as e:
        print("Database error")