from flask import Flask, render_template, Response
import logging
import time

import grpc

import streamServer_pb2
import streamServer_pb2_grpc

channel = grpc.insecure_channel('grpc_server:50051')
stub = streamServer_pb2_grpc.DatastreamerStub(channel)



app = Flask(__name__)


def getAnalytics():
    while True:
        time.sleep(5)
        res = stub.GetAnalytics(streamServer_pb2.DataRequest(name='you'))
        yield f"{res.analytics}\n\n"



@app.route('/')
def index():
    return Response(getAnalytics(), content_type='text/event-stream')



if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)