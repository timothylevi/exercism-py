import re

def is_pangram(sentence):
    """
    Returns true if num of unique letters in sentence equals length of alphabet.
    """
    sentence = re.sub('[\d\W_]+', '', sentence).lower()
    sentence_set = set(sentence)
    alphabet_length = 26

    return len(sentence_set) == alphabet_length
