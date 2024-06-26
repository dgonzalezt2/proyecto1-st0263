# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import filetransfer_pb2 as filetransfer__pb2


class FileServiceStub(object):
    """El servicio que define los métodos RPC que se pueden llamar de forma remota.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendChunk = channel.unary_unary(
                '/filetransfer.FileService/SendChunk',
                request_serializer=filetransfer__pb2.ChunkData.SerializeToString,
                response_deserializer=filetransfer__pb2.TransferStatus.FromString,
                )
        self.RequestChunk = channel.unary_unary(
                '/filetransfer.FileService/RequestChunk',
                request_serializer=filetransfer__pb2.ChunkRequest.SerializeToString,
                response_deserializer=filetransfer__pb2.ChunkData.FromString,
                )
        self.DownloadFromOtherNode = channel.unary_unary(
                '/filetransfer.FileService/DownloadFromOtherNode',
                request_serializer=filetransfer__pb2.ChunkData.SerializeToString,
                response_deserializer=filetransfer__pb2.TransferStatus.FromString,
                )


class FileServiceServicer(object):
    """El servicio que define los métodos RPC que se pueden llamar de forma remota.
    """

    def SendChunk(self, request, context):
        """Método existente para enviar un chunk de archivo.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RequestChunk(self, request, context):
        """Método existente para solicitar un chunk de archivo.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DownloadFromOtherNode(self, request, context):
        """Nuevo método para que un nodo descargue un archivo de otro nodo.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FileServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendChunk': grpc.unary_unary_rpc_method_handler(
                    servicer.SendChunk,
                    request_deserializer=filetransfer__pb2.ChunkData.FromString,
                    response_serializer=filetransfer__pb2.TransferStatus.SerializeToString,
            ),
            'RequestChunk': grpc.unary_unary_rpc_method_handler(
                    servicer.RequestChunk,
                    request_deserializer=filetransfer__pb2.ChunkRequest.FromString,
                    response_serializer=filetransfer__pb2.ChunkData.SerializeToString,
            ),
            'DownloadFromOtherNode': grpc.unary_unary_rpc_method_handler(
                    servicer.DownloadFromOtherNode,
                    request_deserializer=filetransfer__pb2.ChunkData.FromString,
                    response_serializer=filetransfer__pb2.TransferStatus.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'filetransfer.FileService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FileService(object):
    """El servicio que define los métodos RPC que se pueden llamar de forma remota.
    """

    @staticmethod
    def SendChunk(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/filetransfer.FileService/SendChunk',
            filetransfer__pb2.ChunkData.SerializeToString,
            filetransfer__pb2.TransferStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RequestChunk(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/filetransfer.FileService/RequestChunk',
            filetransfer__pb2.ChunkRequest.SerializeToString,
            filetransfer__pb2.ChunkData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DownloadFromOtherNode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/filetransfer.FileService/DownloadFromOtherNode',
            filetransfer__pb2.ChunkData.SerializeToString,
            filetransfer__pb2.TransferStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
