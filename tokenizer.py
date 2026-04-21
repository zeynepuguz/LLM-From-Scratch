import json

class Tokenizer:
    def __init__(self, vocab_file):
        with open(vocab_file, 'r') as f:
            self.vocab = json.load(f)
            self.reverse_vocab = {v: k for k, v in self.vocab.items()}

    def encode(self, text):
        tokens = []
        for word in text.split():
            i = 0
            #examples: "experienced" -> "experi", "enc", "ed"
            while i < len(word):
                found_match = False
                for j in range(len(word), i, -1): # kelimeyi 1 1 azaltarak ilerliyoruz
                    subword = word[i:j]
                    if subword in self.vocab:
                        tokens.append(self.vocab[subword])
                        i = j
                        found_match = True
                        break
                if not found_match:
                    tokens.append(self.vocab["<unk>"])
                    i += 1
            tokens.append(self.vocab[" "]) # kelime sonuna boşluk ekliyoruz
        tokens.pop() # son boşluğu kaldırıyoruz
        return tokens

    def decode(self, ids):
        text = ''
        for id in ids:
            text += self.reverse_vocab[id]
        return text