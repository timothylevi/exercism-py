def distance(strand1, strand2):
    """Return the number of differences between the two DNA strands."""
    if len(strand1) != len(strand2):
        raise ValueError

    differences = 0

    for nucleotide1, nucleotide2 in zip(strand1, strand2):
        if nucleotide1 != nucleotide2:
            differences += 1

    return differences
