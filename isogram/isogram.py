import re

def is_isogram(word):
    """Return true if length of unique chars in word is same length as word."""
    word = re.sub('[\W_]+', '', word).lower()
    chars = set(word)

    return len(chars) == len(word)
