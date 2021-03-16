#from databases import Database
from database.const import DB_USER, DB_HOST, DB_NAME, DB_PASSWORD
import mysql.connector

db = mysql.connector.connect(
        host = DB_HOST,
        user = DB_USER,
        password = DB_PASSWORD,
        database = DB_NAME
)

mycursor = db.cursor()

'''async def connectDB(): #{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}
    #db = Database(f"mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}")
    #await db.connect()
    db = mysql.connector.connect(
        host = DB_HOST,
        user = DB_USER,
        password = DB_PASSWORD,
        database = DB_NAME
    )
    print(f"\n\n\n\n\nMY DB {db}\n\n\n\n\n")
    return db


async def disconnectDB(db):
    await db.disconnect()'''


def execute(query, values) -> bool:  # insert, delete, update
    try:
        
        mycursor.execute(query, values)
        db.commit()
        return True if mycursor.rowcount >= 1 else False

    except Exception as e:
        print("Database error")


def fetch(query) -> list:  # get
    try:
       
        mycursor.execute(query)  
        return mycursor.fetchall()
        

    except Exception as e:
        print("Database error")