def filter_long_words(sentence, n):
    import re
    l = []
    sep = re.split(' ', sentence)
    print(sep)

    for i in sep:
        g = len(i)
        if g > n:
            l.append(i)
        else:
            pass

    return l
