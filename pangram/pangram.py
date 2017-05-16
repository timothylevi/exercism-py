import re, string

def is_pangram(sentence):
    sentence = re.sub('[\d\W_]+', '', sentence).lower()
    alphabet = string.ascii_lowercase

    sentence_set = set(sentence)
    alphabet_set = set(alphabet)

    return len(sentence_set) == len(alphabet_set)
