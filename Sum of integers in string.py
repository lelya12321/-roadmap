def sum_of_integers_in_string(s):
    l = []
    import re
    l.append(re.findall('\d+', s))
    f = l[0]
    result = [sum(int(n) for n in f)]

    for i in result:
        return i