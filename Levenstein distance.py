def levenshtein(a,b):
    return D(len(a) , len(b), a, b)
def some(c, d):
    if c == d:
        return 0
    else:
        return 1

def D(i, j, a, b):
    if i == 0 and j>0:
        return j

    if j ==0 and i>0:
        return i

    if i ==0 and j == 0:
        return 0

    if i>0 and j>0:
        return min((D(i, j -1, a, b) + 1), (D(i - 1, j, a, b)+1),(D(i -1, j - 1, a,b ) + some(a[i -1 ] , b[j - 1])))