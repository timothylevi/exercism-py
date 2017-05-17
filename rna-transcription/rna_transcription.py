def to_rna(sequence):
    complements = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U'
    }

    try:
        sequence = [complements[nucleotide] for nucleotide in sequence]
    except KeyError as e:
        return ''

    return ''.join(sequence)
