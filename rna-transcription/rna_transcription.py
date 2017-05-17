COMPLEMENTS = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U'
}

def to_rna(sequence):
    """"
    If an input is invalid, return empty string. Otherwise, return a string
    with each DNA nucleotide replaced with it's complementary RNA nucleotide.
    """
    try:
        return ''.join([COMPLEMENTS[nucleotide] for nucleotide in sequence])
    except KeyError as e:
        return ''
