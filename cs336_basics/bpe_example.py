import regex as re

TEXT = """
low low low low low
lower lower lower lower lower
newest newest newest newest newest 
"""

def initialize_vocab():
    byte_dict = {i: bytes([i]) for i in range(256)}
    byte_dict[256] = "<|endoftext|>"
    return byte_dict

def pretokenize(text) -> dict[tuple[bytes, ...], int]:
    PAT = r"""'(?:[sdmt]|ll|ve|re)| ?\p{L}+| ?\p{N}+| ?[^\s\p{L}\p{N}]+|\s+(?!\S)|\s+"""
    text_iter = re.finditer(PAT, text)
    pretoken_dict = {}
    for t in text_iter:
        encoded = tuple(t.group(0).encode("utf-8"))
        if encoded not in pretoken_dict:
            pretoken_dict[encoded] = 1
        else:
            pretoken_dict[t.match.encode("utf-8")] += 1
    return pretoken_dict

if __name__ == "__main__":
    vocab_dict = initialize_vocab()
    pretokenization = pretokenize(TEXT)
    
