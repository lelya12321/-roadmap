import re

def valid_parentheses(string):
    a = "()"
    str__ = re.sub(r'\w*\s*', '', string)

    while True:
        if a in str__:
            str__ = str__.replace('()', '')
        else:
            break
    return len(str__) == 0
