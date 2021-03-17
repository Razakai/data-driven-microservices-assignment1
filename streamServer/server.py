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
import random

import streamServer_pb2
import streamServer_pb2_grpc
import pandas as pd


class Datastreamer(streamServer_pb2_grpc.DatastreamerServicer):
    def GetData(self, request, context):
        dataframe = pd.read_csv('r_dataisbeautiful_posts.csv')
        for idx, line in enumerate(dataframe.values):
            if idx % 2 == 0:
                time.sleep(random.randint(1, 5))
            
            arr = [str(val) for val in line]
            
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


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    streamServer_pb2_grpc.add_DatastreamerServicer_to_server(Datastreamer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
