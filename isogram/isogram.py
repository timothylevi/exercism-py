import re

def is_isogram(word):
    if len(word) == 0:
        return True

    stash = {}
    word = re.sub('[\W_]+', '', word).lower()

    for char in word:
        if stash.get(char):
            return False

        stash[char] = True

    return True
