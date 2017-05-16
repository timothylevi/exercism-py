import re

def is_isogram(word):
    word = re.sub('[\W_]+', '', word).lower()
    chars = set(word)

    return len(chars) == len(word)
