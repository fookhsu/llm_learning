from build import node_strategy_pb2
# from mindspore.train.node_strategy_pb2 import ParallelStrategyMap as ckpt_strategy
"""
message ParallelLayouts {
    repeated DevMatrix dev_matrix = 1;
    repeated TensorMap tensor_map = 2;
    repeated ParamSplitShape param_split_shape = 3;
    repeated IndicesOffset indices_offset = 4;
    required int32 field = 5;
    required int32 opt_weight_shard_step = 6;
    required int32 opt_weight_shard_size = 7;
}
"""
def create_and_serialize_parallel_layouts():
    # 创建 ParallelLayouts 实例
    parallel_layouts = node_strategy_pb2.ParallelLayouts()

    # 添加 DevMatrix
    dev_matrix = parallel_layouts.dev_matrix.add()
    dev_matrix.dim.extend([2, 2])  # 示例数据

    # 添加 TensorMap
    tensor_map = parallel_layouts.tensor_map.add()
    tensor_map.dim.extend([1, 1])  # 示例数据

    # 添加 ParamSplitShape
    param_split_shape = parallel_layouts.param_split_shape.add()
    param_split_shape.dim.extend([4, 4])  # 示例数据

    # 添加 IndicesOffset
    indices_offset = parallel_layouts.indices_offset.add()
    indices_offset.dim.extend([1, 2])  # 示例数据

    # 设置 required 字段
    parallel_layouts.field = 10
    parallel_layouts.opt_weight_shard_step = 20
    parallel_layouts.opt_weight_shard_size = 30

    # 序列化为字节字符串
    serialized_data = parallel_layouts.SerializeToString()
    return serialized_data

def deserialize_parallel_layouts(serialized_data):
    # 创建一个新的 ParallelLayouts 实例
    parallel_layouts = node_strategy_pb2.ParallelLayouts()

    # 解析字节字符串到新的实例中
    parallel_layouts.ParseFromString(serialized_data)

    # 验证解析的数据
    for dev_matrix in parallel_layouts.dev_matrix:
        print("DevMatrix:", dev_matrix.dim)

    for tensor_map in parallel_layouts.tensor_map:
        print("TensorMap:", tensor_map.dim)

    for param_split_shape in parallel_layouts.param_split_shape:
        print("ParamSplitShape:", param_split_shape.dim)

    for indices_offset in parallel_layouts.indices_offset:
        print("IndicesOffset:", indices_offset.dim)

    print("Field:", parallel_layouts.field)
    print("OptWeightShardStep:", parallel_layouts.opt_weight_shard_step)
    print("OptWeightShardSize:", parallel_layouts.opt_weight_shard_size)

def main():
    serialized_data = create_and_serialize_parallel_layouts()
    print("Serialized data:", serialized_data)
    deserialize_parallel_layouts(serialized_data)
    

if __name__ == "__main__":
    main()