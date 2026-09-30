import torch
import torch.nn as nn

def create_embedding_layer(vocab_size: int, d_model: int) -> nn.Embedding:
    """
    Returns an embedding layer with the requested dimensions.
    """
    return nn.Embedding(num_embeddings=vocab_size, embedding_dim=d_model)

def embed_tokens(embedding: nn.Embedding, tokens: torch.Tensor, d_model: int) -> torch.Tensor:
    """
    Returns scaled token embeddings.
    """
    final_embed = torch.empty(len(tokens), d_model)
    for i, token in enumerate(tokens):
         final_embed[i] = embedding(token) * (d_model ** 0.5)

    return final_embed