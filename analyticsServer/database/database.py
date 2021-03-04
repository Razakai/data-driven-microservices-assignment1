from databases import Database
from database.const import DB_USER, DB_HOST, DB_NAME, DB_PASSWORD


async def connectDB(): #{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}
    db = Database(f"mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}")
    await db.connect()
    return db


async def disconnectDB(db):
    await db.disconnect()


async def execute(query, isMany, values=None) -> bool:  # insert, delete, update
    db = await connectDB()
    try:
        if isMany:
            res = await db.execute_many(query=query, values=values)

        else:
            res = await db.execute(query=query, values=values)

        await disconnectDB(db)
        return True if res >= 1 else False

    except Exception as e:
        await disconnectDB(db)


async def fetch(query, isOne, values=None) -> list:  # get
    db = await connectDB()
    try:
        if isOne:
            res = await db.fetch_one(query=query, values=values)

        else:
            res = await db.fetch_all(query=query, values=values)

        await disconnectDB(db)
        return res

    except Exception as e:
        await disconnectDB(db)