# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: filetransfer.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x66iletransfer.proto\x12\x0c\x66iletransfer\"G\n\tChunkData\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x14\n\x0c\x63hunk_number\x18\x02 \x01(\x05\x12\x12\n\nchunk_data\x18\x03 \x01(\x0c\"L\n\x0eTransferStatus\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x18\n\x10new_free_storage\x18\x03 \x01(\x02\"6\n\x0c\x43hunkRequest\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x14\n\x0c\x63hunk_number\x18\x02 \x01(\x05\x32\xe6\x01\n\x0b\x46ileService\x12\x42\n\tSendChunk\x12\x17.filetransfer.ChunkData\x1a\x1c.filetransfer.TransferStatus\x12\x43\n\x0cRequestChunk\x12\x1a.filetransfer.ChunkRequest\x1a\x17.filetransfer.ChunkData\x12N\n\x15\x44ownloadFromOtherNode\x12\x17.filetransfer.ChunkData\x1a\x1c.filetransfer.TransferStatusb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'filetransfer_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_CHUNKDATA']._serialized_start=36
  _globals['_CHUNKDATA']._serialized_end=107
  _globals['_TRANSFERSTATUS']._serialized_start=109
  _globals['_TRANSFERSTATUS']._serialized_end=185
  _globals['_CHUNKREQUEST']._serialized_start=187
  _globals['_CHUNKREQUEST']._serialized_end=241
  _globals['_FILESERVICE']._serialized_start=244
  _globals['_FILESERVICE']._serialized_end=474
# @@protoc_insertion_point(module_scope)