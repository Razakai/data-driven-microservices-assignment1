from database.database import fetch

def getData() -> list:
    query = "SELECT * FROM data"
    res = fetch(query)
    return res


