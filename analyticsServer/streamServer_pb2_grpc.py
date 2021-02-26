# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import streamServer_pb2 as streamServer__pb2


class DatastreamerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetData = channel.unary_stream(
                '/streamServer.Datastreamer/GetData',
                request_serializer=streamServer__pb2.DataRequest.SerializeToString,
                response_deserializer=streamServer__pb2.DataResponse.FromString,
                )
        self.UpdateRealTimeAnalytics = channel.unary_unary(
                '/streamServer.Datastreamer/UpdateRealTimeAnalytics',
                request_serializer=streamServer__pb2.RealTimeAnalyticsRequest.SerializeToString,
                response_deserializer=streamServer__pb2.Confirmation.FromString,
                )
        self.UpdateRollingAnalytics = channel.unary_unary(
                '/streamServer.Datastreamer/UpdateRollingAnalytics',
                request_serializer=streamServer__pb2.RollingAnalyticsRequest.SerializeToString,
                response_deserializer=streamServer__pb2.Confirmation.FromString,
                )
        self.GetAnalytics = channel.unary_unary(
                '/streamServer.Datastreamer/GetAnalytics',
                request_serializer=streamServer__pb2.DataRequest.SerializeToString,
                response_deserializer=streamServer__pb2.AnalyticsResponse.FromString,
                )


class DatastreamerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateRealTimeAnalytics(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateRollingAnalytics(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAnalytics(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DatastreamerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetData': grpc.unary_stream_rpc_method_handler(
                    servicer.GetData,
                    request_deserializer=streamServer__pb2.DataRequest.FromString,
                    response_serializer=streamServer__pb2.DataResponse.SerializeToString,
            ),
            'UpdateRealTimeAnalytics': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateRealTimeAnalytics,
                    request_deserializer=streamServer__pb2.RealTimeAnalyticsRequest.FromString,
                    response_serializer=streamServer__pb2.Confirmation.SerializeToString,
            ),
            'UpdateRollingAnalytics': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateRollingAnalytics,
                    request_deserializer=streamServer__pb2.RollingAnalyticsRequest.FromString,
                    response_serializer=streamServer__pb2.Confirmation.SerializeToString,
            ),
            'GetAnalytics': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAnalytics,
                    request_deserializer=streamServer__pb2.DataRequest.FromString,
                    response_serializer=streamServer__pb2.AnalyticsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'streamServer.Datastreamer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Datastreamer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/streamServer.Datastreamer/GetData',
            streamServer__pb2.DataRequest.SerializeToString,
            streamServer__pb2.DataResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateRealTimeAnalytics(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/streamServer.Datastreamer/UpdateRealTimeAnalytics',
            streamServer__pb2.RealTimeAnalyticsRequest.SerializeToString,
            streamServer__pb2.Confirmation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateRollingAnalytics(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/streamServer.Datastreamer/UpdateRollingAnalytics',
            streamServer__pb2.RollingAnalyticsRequest.SerializeToString,
            streamServer__pb2.Confirmation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAnalytics(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/streamServer.Datastreamer/GetAnalytics',
            streamServer__pb2.DataRequest.SerializeToString,
            streamServer__pb2.AnalyticsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
