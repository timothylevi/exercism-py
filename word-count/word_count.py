import re
from collections import defaultdict

def word_count(phrase):
    """
    Replace spaces, non-alphanumeric, and underscore characters with tab
    set case of phrase to lowercase and split using default pattern. Returns
    a dictionary with words as keys and counts as values.
    """

    phrase = re.sub(r'[\s\W_]+', '\t', phrase).lower().split()
    words = defaultdict(lambda: 0)

    for word in phrase:
        words[word] = words[word] + 1

    return dict(words)
