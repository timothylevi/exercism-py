def distance(strand1, strand2):
    """Return the number of differences between the two DNA strands."""
    if len(strand1) != len(strand2):
        raise ValueError

    differences = 0

    for index, char in enumerate(strand1):
        if char != strand2[index]:
            differences += 1

    return differences
