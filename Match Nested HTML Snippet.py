import re

def matches(snippet):
    lst_without = re.findall(r'<\w*>', snippet)
    lst_with = re.findall(r'<\/\w*>', snippet)
    lst_with_2 = [item.replace('/', '') for item in lst_with]

    s = [item for item in lst_without if not item in lst_with_2 or lst_with_2.remove(item)]
    return len(s) == 0