from database.database import fetch, execute

async def getData() -> dict:
    query = "SELECT * FROM data"
    res = await fetch(query=query, isOne=True)
    return dict(res) if res is not None else {}


async def setData(avgWordsPerPost, postWithMostWords, authorWithMostDeletedPosts, avgWordLength=None) -> None:
    query = ""
    values = {}
    if avgWordLength is not None:


        query = """UPDATE data 
        SET
        avgWordsPerPost = :avgWordsPerPost,
        postWithMostWords = :postWithMostWords,
        authorWithMostDeletedPosts = :authorWithMostDeletedPosts,
        avgWordLength = :avgWordLength
        WHERE rowID = 1
        """
        values = {"avgWordsPerPost": avgWordsPerPost, "postWithMostWords": postWithMostWords, "authorWithMostDeletedPosts": authorWithMostDeletedPosts, "avgWordLength": avgWordLength}
    else:
        query = """UPDATE data 
        SET
        avgWordsPerPost = :avgWordsPerPost,
        postWithMostWords = :postWithMostWords,
        authorWithMostDeletedPosts = :authorWithMostDeletedPosts
        WHERE rowID = 1
        """
        values = {"avgWordsPerPost": avgWordsPerPost, "postWithMostWords": postWithMostWords, "authorWithMostDeletedPosts": authorWithMostDeletedPosts}
    
    await execute(query=query, isMany=False, values=values)

