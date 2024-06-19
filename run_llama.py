from transformers.models.llama import LlamaModel, LlamaConfig
import torch

def run_llama():
    llama_config = LlamaConfig(vocab_size=32000, hidden_size=4096//2,
                              intermediate_size=11008//2,
                              num_hidden_layers=32//2,
                              num_attention_heads=32//2,
                              max_position_embeddings=2048//2)
    llama_model = LlamaModel(config=llama_config)

    inputs_ids = torch.randint(
        low=0, high=llama_config.vocab_size, size=(4, 30)
    )

    res = llama_config(inputs_ids)
    print(res)

if __name__ == '__main__':
    run_llama()