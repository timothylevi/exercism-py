import re

def is_isogram(word):
    word = re.sub('[\W_]+', '', word).lower()
    chars = set()

    for char in word:
        if char in chars:
            return False

        chars.add(char)

    return True
