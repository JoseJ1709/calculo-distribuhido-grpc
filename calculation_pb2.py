# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: calculation.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'calculation.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x63\x61lculation.proto\x12\x0b\x63\x61lculation\"X\n\x12\x43\x61lculationRequest\x12\x0f\n\x07number1\x18\x01 \x01(\x05\x12\x0f\n\x07number2\x18\x02 \x01(\x05\x12\x0f\n\x07number3\x18\x03 \x01(\x05\x12\x0f\n\x07number4\x18\x04 \x01(\x05\"%\n\x13\x43\x61lculationResponse\x12\x0e\n\x06result\x18\x01 \x01(\x05\x32g\n\x12\x43\x61lculationService\x12Q\n\x0c\x43\x61lculateSum\x12\x1f.calculation.CalculationRequest\x1a .calculation.CalculationResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'calculation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CALCULATIONREQUEST']._serialized_start=34
  _globals['_CALCULATIONREQUEST']._serialized_end=122
  _globals['_CALCULATIONRESPONSE']._serialized_start=124
  _globals['_CALCULATIONRESPONSE']._serialized_end=161
  _globals['_CALCULATIONSERVICE']._serialized_start=163
  _globals['_CALCULATIONSERVICE']._serialized_end=266
# @@protoc_insertion_point(module_scope)
