from database.queries import getData, setData
from database.database import execute
import time


#setData("qqqq", "wwww", "eeee")


while True:
        print(getData(), '\n\n\n\n\n')
        time.sleep(2)


'''query = """UPDATE data 
        SET
        avgWordsPerPost = %s,
        postWithMostWords = %s,
        authorWithMostDeletedPosts = %s
        WHERE rowID = 1
        """

print(execute(query, ("qqqqq", "wwwww", "eeeee")))'''