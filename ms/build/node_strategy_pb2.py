# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: node_strategy.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13node_strategy.proto\"\x1f\n\x10ParallelStrategy\x12\x0b\n\x03\x64im\x18\x01 \x03(\r\"P\n\x11ParallelStrategys\x12\r\n\x05stage\x18\x01 \x02(\r\x12,\n\x11parallel_strategy\x18\x02 \x03(\x0b\x32\x11.ParallelStrategy\"Y\n\x14ParallelStrategyItem\x12\x11\n\tnode_name\x18\x01 \x02(\t\x12.\n\x12parallel_strategys\x18\x02 \x02(\x0b\x32\x12.ParallelStrategys\"\x18\n\tDevMatrix\x12\x0b\n\x03\x64im\x18\x01 \x03(\r\"\x18\n\tTensorMap\x12\x0b\n\x03\x64im\x18\x01 \x03(\x05\"\x1e\n\x0fParamSplitShape\x12\x0b\n\x03\x64im\x18\x01 \x03(\x03\"\x1c\n\rIndicesOffset\x12\x0b\n\x03\x64im\x18\x01 \x03(\x03\"\xf3\x01\n\x0fParallelLayouts\x12\x1e\n\ndev_matrix\x18\x01 \x03(\x0b\x32\n.DevMatrix\x12\x1e\n\ntensor_map\x18\x02 \x03(\x0b\x32\n.TensorMap\x12+\n\x11param_split_shape\x18\x03 \x03(\x0b\x32\x10.ParamSplitShape\x12&\n\x0eindices_offset\x18\x04 \x03(\x0b\x32\x0e.IndicesOffset\x12\r\n\x05\x66ield\x18\x05 \x02(\x05\x12\x1d\n\x15opt_weight_shard_step\x18\x06 \x02(\x05\x12\x1d\n\x15opt_weight_shard_size\x18\x07 \x02(\x05\"T\n\x12ParallelLayoutItem\x12\x12\n\nparam_name\x18\x01 \x02(\t\x12*\n\x10parallel_layouts\x18\x02 \x02(\x0b\x32\x10.ParallelLayouts\"!\n\x12ParallelGroupRanks\x12\x0b\n\x03\x64im\x18\x01 \x03(\r\"Z\n\x11ParallelGroupItem\x12\x12\n\ngroup_name\x18\x01 \x02(\t\x12\x31\n\x14parallel_group_ranks\x18\x02 \x02(\x0b\x32\x13.ParallelGroupRanks\"x\n\x10ParallelGroupMap\x12/\n\x13parallel_group_item\x18\x01 \x03(\x0b\x32\x12.ParallelGroupItem\x12\x33\n\x16\x63kpt_restore_rank_list\x18\x02 \x02(\x0b\x32\x13.ParallelGroupRanks\"\x96\x01\n\x13ParallelStrategyMap\x12\x15\n\rcurrent_stage\x18\x01 \x02(\r\x12\x35\n\x16parallel_strategy_item\x18\x02 \x03(\x0b\x32\x15.ParallelStrategyItem\x12\x31\n\x14parallel_layout_item\x18\x03 \x03(\x0b\x32\x13.ParallelLayoutItem')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'node_strategy_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PARALLELSTRATEGY._serialized_start=23
  _PARALLELSTRATEGY._serialized_end=54
  _PARALLELSTRATEGYS._serialized_start=56
  _PARALLELSTRATEGYS._serialized_end=136
  _PARALLELSTRATEGYITEM._serialized_start=138
  _PARALLELSTRATEGYITEM._serialized_end=227
  _DEVMATRIX._serialized_start=229
  _DEVMATRIX._serialized_end=253
  _TENSORMAP._serialized_start=255
  _TENSORMAP._serialized_end=279
  _PARAMSPLITSHAPE._serialized_start=281
  _PARAMSPLITSHAPE._serialized_end=311
  _INDICESOFFSET._serialized_start=313
  _INDICESOFFSET._serialized_end=341
  _PARALLELLAYOUTS._serialized_start=344
  _PARALLELLAYOUTS._serialized_end=587
  _PARALLELLAYOUTITEM._serialized_start=589
  _PARALLELLAYOUTITEM._serialized_end=673
  _PARALLELGROUPRANKS._serialized_start=675
  _PARALLELGROUPRANKS._serialized_end=708
  _PARALLELGROUPITEM._serialized_start=710
  _PARALLELGROUPITEM._serialized_end=800
  _PARALLELGROUPMAP._serialized_start=802
  _PARALLELGROUPMAP._serialized_end=922
  _PARALLELSTRATEGYMAP._serialized_start=925
  _PARALLELSTRATEGYMAP._serialized_end=1075
# @@protoc_insertion_point(module_scope)
