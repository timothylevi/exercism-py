import re

def hey(expression):
    """Returns a different response based on the type of expression."""
    expression = expression.strip()
    expression_subbed = re.sub('[\d\W_]+', '', expression)

    is_question = expression.endswith("?")
    is_exclamation = expression == expression.upper() and expression_subbed

    if not expression:
        return "Fine. Be that way!"
    elif is_exclamation:
        return "Whoa, chill out!"
    elif is_question:
        return "Sure."

    return "Whatever."
