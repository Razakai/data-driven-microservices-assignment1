from __future__ import print_function
import logging

import grpc
import time

import streamServer_pb2
import streamServer_pb2_grpc
from database.queries import setData, getData



def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.

    # Metric 1
    # aggregate metric - average number of words per post
    totalPosts = 0
    totalWords = 0

    # Metric 2
    # rolling 3 minute metric - average word length
    startTime = time.time()
    threeMinWordCount = 0
    numLetters = 0

    # Metric 3
    # post with some criteria - most words
    longestTitle = ""
    mostWordsInTitle = 0

    # Metric 4
    # metric not based on post title - author with most deleted posts
    authorDict = {}
    authorWithMostDeletedPosts = ""

    #with grpc.insecure_channel('grpc_server:50051') as channel:
    with grpc.insecure_channel('grpc_server:50051') as channel:
        stub = streamServer_pb2_grpc.DatastreamerStub(channel)
        for line in stub.GetData(streamServer_pb2.DataRequest(name='you')):
            # Metric 1

            title = line.title.strip()
            words = title.split(" ")
            totalWords += len(words)
            totalPosts += 1

            # Metric 3
            if len(words) > mostWordsInTitle:
                mostWordsInTitle = len(words)
                longestTitle = title

            
            # Metric 4
            if line.removed_by != "nan" and line.author != "[deleted]":
                if line.author in authorDict.keys():
                    authorDict[line.author] += 1
                else:
                    authorDict[line.author] = 1
            
                authorDict = dict(sorted(authorDict.items(), key=lambda item: item[1], reverse=True))
                for key in authorDict.keys():
                    authorWithMostDeletedPosts = key
                    break

             # Metric 2
            # Reset every 3 min
            if (int(time.time() - startTime)) >= 180:
                setData(str(int(totalWords/totalPosts)), str(longestTitle), str(authorWithMostDeletedPosts), str(int(numLetters/threeMinWordCount)))

                startTime = time.time()
                threeMinWordCount = 0
                numLetters = 0
            
            else:
                setData(str(int(totalWords/totalPosts)), str(longestTitle), str(authorWithMostDeletedPosts))

            threeMinWordCount += len(words)
            numLetters += len(list(''.join(words)))


if __name__ == '__main__':
    logging.basicConfig()
    run()
