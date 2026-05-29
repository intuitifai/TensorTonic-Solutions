def text_chunking(tokens, chunk_size, overlap):
    if tokens == []:
        return []
    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    if len(tokens) <= chunk_size:
        return [tokens]

    final = []
    step = chunk_size - overlap
    i = 0

    while i + chunk_size <= len(tokens):
        final.append(tokens[i:i + chunk_size])
        i += step

    return final