class SimpleTokenizer:
    def __init__(self):
        self.word_to_id = {}
        self.id_to_word = {}
        self.vocab_size = 0
        self.pad_token = "<PAD>"
        self.unk_token = "<UNK>"
        self.bos_token = "<BOS>"
        self.eos_token = "<EOS>"

    def build_vocab(self, texts: list[str]) -> None:
        """
        Builds the vocabulary in place.
        """
        self.word_to_id[self.pad_token] = 0
        self.word_to_id[self.unk_token] = 1
        self.word_to_id[self.bos_token] = 2
        self.word_to_id[self.eos_token] = 3
        unique_string = set()
        for text in texts:
            for word in text.lower().split():
                unique_string.add(word)
        sorted_words = sorted(unique_string)
        for i, word in enumerate(sorted_words, start=4):
            lower_word = word.lower()
            self.word_to_id[lower_word] = i
        self.id_to_word = {value: key for key, value in self.word_to_id.items()}
        self.vocab_size = len(self.word_to_id)
            

    def encode(self, text: str) -> list[int]:
        """
        Returns token IDs for the input text.
        """
        encoded_out = []
        for word in text.lower().split():
            if word not in self.word_to_id:
                encoded_out.append(self.word_to_id[self.unk_token])
            else:
                encoded_out.append(self.word_to_id[word])
        return encoded_out

    def decode(self, ids: list[int]) -> str:
        """
        Returns the decoded, space-separated text.
        """
        decoded_out = []
        for id in ids:
            if id not in self.id_to_word:
                decoded_out.append(self.unk_token)
            else:
                decoded_out.append(self.id_to_word[id])
        return ' '.join(decoded_out)