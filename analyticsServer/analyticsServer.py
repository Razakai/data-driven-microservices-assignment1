from __future__ import print_function
import logging

import grpc

import streamServer_pb2
import streamServer_pb2_grpc



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
    itteration = 0
    timePerItter = 5
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

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = streamServer_pb2_grpc.DatastreamerStub(channel)
        #response = stub.GetData(streamServer_pb2.DataRequest(name='you'))
        for line in stub.GetData(streamServer_pb2.DataRequest(name='you')):
            # Metric 1
            title = line.title.strip()
            words = title.split(" ")
            totalWords += len(words)
            totalPosts += 1

            # Metric 2
            itteration += 1

            # Reset every 3 min
            if (timePerItter * itteration) >= 180:
                stub.UpdateRollingAnalytics(streamServer_pb2.RollingAnalyticsRequest(
                    avgWordLength=str(int(numLetters/threeMinWordCount))
                ))

                itteration = 0
                threeMinWordCount = 0
                numLetters = 0

            
            threeMinWordCount += len(words)
            numLetters += len(list(''.join(words)))

            # Metric 3
            if len(words) > mostWordsInTitle:
                mostWordsInTitle = len(words)
                longestTitle = line.title

            
            # Metric 4
            if line.removed_by != "nan":
                if line.author in authorDict.keys():
                    authorDict[line.author] += 1
                else:
                    authorDict[line.author] = 1
            
            authorDict = dict(sorted(authorDict.items(), key=lambda item: item[1], reverse=True))
            for key in authorDict.keys():
                authorWithMostDeletedPosts = key
                break
            
            # UpdateRealTimeAnalytics
            stub.UpdateRealTimeAnalytics(streamServer_pb2.RealTimeAnalyticsRequest(
                avgWordsPerPost=str(int(totalWords/totalPosts)),
                postWithMostWords=str(longestTitle),
                authorWithMostDeletedPosts=str(authorWithMostDeletedPosts)
            ))

        

if __name__ == '__main__':
    logging.basicConfig()
    run()
