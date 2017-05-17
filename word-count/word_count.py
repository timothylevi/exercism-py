import re
from collections import Counter

def word_count(phrase):
    """
    Replace spaces, non-alphanumeric, and underscore characters with tab
    set case of phrase to lowercase and split using default pattern. Returns
    a Counter with words as keys and counts as values.
    """
    phrase = re.sub(r'[\s\W_]+', '\t', phrase).lower().split()
    return Counter(phrase)
