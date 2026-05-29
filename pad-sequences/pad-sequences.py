import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    updated_seqs = []
    if max_len == None:
        max_len = max(len(seq) for seq in seqs)
    for seq in seqs:
        seq_len = len(seq)
        # 3 cases
        # seq_len > max_len; truncate
        if seq_len > max_len:
            updated_seqs.append(seq[: max_len])
        # seq_len < max_len; append pad_value
        elif seq_len < max_len:
            padding_length = max_len - seq_len
            for i in range(padding_length):
                seq.append(pad_value)
            updated_seqs.append(seq)
        # seq_len == max_len; do not do anything
        else:
            updated_seqs.append(seq)
    return updated_seqs
    