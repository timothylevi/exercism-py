COMPLEMENTS = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U'
}

def get_rna_complement(nucleotide):
    """Return the RNA complement to the DNA nucleotide."""
    return COMPLEMENTS[nucleotide]

def to_rna(sequence):
    """"
    If an input is invalid, return empty string. Otherwise, return a string
    with each DNA nucleotide replaced with it's complementary RNA nucleotide.
    """
    try:
        sequence = [get_rna_complement(nucleotide) for nucleotide in sequence]
        return ''.join(sequence)
    except KeyError as e:
        return ''
