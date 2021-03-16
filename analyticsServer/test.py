from database.queries import getData
from database.database import execute


getData()


'''query = """UPDATE data 
        SET
        avgWordsPerPost = %s,
        postWithMostWords = %s,
        authorWithMostDeletedPosts = %s
        WHERE rowID = 1
        """

print(execute(query, ("qqqqq", "wwwww", "eeeee")))'''