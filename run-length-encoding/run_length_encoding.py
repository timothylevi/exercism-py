def decode(doc):
    encoded = []
    times = 0

    for char in doc:
        if char.isdigit():
            times = times * 10 + int(char)
        elif char.isalnum() or char.isspace():
            for i in range(times if times else 1):
                encoded.append(char)
            times = 0

    return ''.join(encoded)


def encode(doc):
    decoded = []

    count = 0
    letter = ""

    for char in doc:
        if char == letter:
            count += 1
        else:
            decoded.append(str(count) if count > 1 else '')
            decoded.append(letter)
            letter = char
            count = 1

    decoded.append(str(count) if count > 1 else '')
    decoded.append(letter)

    return ''.join(decoded)
