from database.database import fetch, execute

def getData() -> None:
    query = "SELECT * FROM data"
    res = fetch(query)
    print(res)


def setData(avgWordsPerPost, postWithMostWords, authorWithMostDeletedPosts, avgWordLength=None) -> None:
    query = ""
    values = ()
    if avgWordLength is not None:

        query = """UPDATE data 
        SET
        avgWordsPerPost = %s,
        postWithMostWords = %s,
        authorWithMostDeletedPosts = %s,
        avgWordLength = %s
        WHERE rowID = 1
        """
        values = (avgWordsPerPost, postWithMostWords, authorWithMostDeletedPosts, avgWordLength)
    else:
        query = """UPDATE data 
        SET
        avgWordsPerPost = %s,
        postWithMostWords = %s,
        authorWithMostDeletedPosts = %s
        WHERE rowID = 1
        """
        values = (avgWordsPerPost, postWithMostWords, authorWithMostDeletedPosts)
    
    execute(query, values)

