# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import logging
import time
import grpc

import streamServer_pb2
import streamServer_pb2_grpc
import pandas as pd


class Datastreamer(streamServer_pb2_grpc.DatastreamerServicer):
    def __init__(self):
        self.avgWordsPerPost = ""
        self.postWithMostWords = ""
        self.authorWithMostDeletedPosts = ""
        self.avgWordLength = ""


    def GetData(self, request, context):
        dataframe = pd.read_csv('r_dataisbeautiful_posts.csv')
        for line in dataframe.values:
            arr = [str(val) for val in line]
            time.sleep(5)
            yield streamServer_pb2.DataResponse(
                id=arr[0],
                title=arr[1],
                score=arr[2],
                author=arr[3],
                author_flair_text=arr[4],
                removed_by=arr[5],
                total_awards_received=arr[6],
                awarders=arr[7],
                created_utc=arr[8],
                full_link=arr[9],
                num_comments=arr[10],
                over_18=arr[11])
    
    def UpdateRealTimeAnalytics(self, request, context):
        self.avgWordsPerPost = request.avgWordsPerPost
        self.postWithMostWords = request.postWithMostWords
        self.authorWithMostDeletedPosts = request.authorWithMostDeletedPosts
        #print(self.avgWordsPerPost, self.postWithMostWords, self.authorWithMostDeletedPosts)

        return streamServer_pb2.Confirmation(confirm="True")
    

    def UpdateRollingAnalytics(self, request, context):
        self.avgWordLength = request.avgWordLength
        #print(self.avgWordLength)

        return streamServer_pb2.Confirmation(confirm="True")
    

    def GetAnalytics(self, request, context):
        return streamServer_pb2.AnalyticsResponse(
            analytics=f'Average words per post: {self.avgWordsPerPost}\nPost title with most words: {self.postWithMostWords}\nAuthor with most deleted posts: {self.authorWithMostDeletedPosts}\nAverage word length: {self.avgWordLength}\n')

        
        #return streamServer_pb2.DataResponse(message='Hello, %s!' % request.name)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    streamServer_pb2_grpc.add_DatastreamerServicer_to_server(Datastreamer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
