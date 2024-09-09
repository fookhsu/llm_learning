from transformers import AutoTokenizer

# tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
tokenizer = AutoTokenizer.from_pretrained("./bert/")
print(tokenizer.backend_tokenizer.normalizer.normalize_str("Héllò hôw are ü?"))

# AutoTokenizer 类在 transformers/src/transformers/models/auto/tokenization_auto.py
"""
    ----> 1
    tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")
    tokenizer.save_pretrained("tokenizer-test")
    
    ----> 2 获取tokenizer_config.json 文件
    tokenizer_config = get_tokenizer_config("tokenizer-test")
    get_tokenizer_config --> tokenizer_config.json
    
    ----> 3 
    获取 config.json
    1. transformers/src/transformers/models/auto/configuration_auto.py
    config = AutoConfig.from_pretrained(
    pretrained_model_name_or_path,
    trust_remote_code=trust_remote_code,
    **kwargs,
    )
    2.
    config_dict, unused_kwargs = PretrainedConfig.get_config_dict(pretrained_model_name_or_path, **kwargs)
    
    3. transformers/src/transformers/configuration_utils.py
    if "auto_map" in config_dict and not is_local:
    config_dict["auto_map"] = add_model_info_to_auto_map(
        config_dict["auto_map"], pretrained_model_name_or_path
    )
    
    if has_remote_code and trust_remote_code:
    class_ref = config_dict["auto_map"]["AutoConfig"]
    config_class = get_class_from_dynamic_module(
        class_ref, pretrained_model_name_or_path, code_revision=code_revision, **kwargs
    )
    ----> 4 获取model config class
    # local
    if os.path.isdir(pretrained_model_name_or_path):
        config_class.register_for_auto_class()
    return config_class.from_pretrained(pretrained_model_name_or_path, **kwargs)
    # remote 从config.json --> "model_type": "bert" --> BertConfig
    elif "model_type" in config_dict:
    config_class = CONFIG_MAPPING[config_dict["model_type"]]
    return config_class.from_dict(config_dict, **unused_kwargs) # from_dict 使用config_dict初始化Config
    
    ----> 5 获取tokenizer class
    # 部分模型没有 如果有 从远端或者本地获取
    get_class_from_dynamic_module
    # 没有
    #  model_type: BertConfig
    # BertTokenizer 
    model_type = config_class_to_model_type(type(config).__name__)
    # BertTokenizer BertTokenizerFast
    tokenizer_class_py, tokenizer_class_fast = TOKENIZER_MAPPING[type(config)]
    # BertTokenizer.from_pretrained
    return tokenizer_class_py.from_pretrained(
        pretrained_model_name_or_path, *inputs, **kwargs
    )
    ----> 6 
    # transformers/src/transformers/tokenization_utils_base.py
    # BertTokenizer --> PreTrainedTokenizer --> PreTrainedTokenizerBase
    
    # Slow tokenizers used to be saved in three separated files
    SPECIAL_TOKENS_MAP_FILE = "special_tokens_map.json"
    ADDED_TOKENS_FILE = "added_tokens.json"
    TOKENIZER_CONFIG_FILE = "tokenizer_config.json"

    # Fast tokenizers (provided by HuggingFace tokenizer's library) can be saved in a single file
    FULL_TOKENIZER_FILE = "tokenizer.json"
    {'vocab_file': 'vocab.txt', 'tokenizer_file': 'tokenizer.json', 'added_tokens_file': 'added_tokens.json', 'special_tokens_map_file': 'special_tokens_map.json', 'tokenizer_config_file': 'tokenizer_config.json'}
    
    cls._from_pretrained
"""
