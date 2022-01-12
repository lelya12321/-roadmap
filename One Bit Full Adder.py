def one_bit_full_adder(cin, a, b):
    f = []
    if a+b+cin ==1:
        f.append(0)
        f.append(1)
        return tuple(f)
    if a+b+cin ==0:
        f.append(0)
        f.append(0)
        return tuple(f)
    if a+b+cin==2:
        f.append(1)
        f.append(0)
        return tuple(f)
    if a+b+cin==3:
        f.append(1)
        f.append(1)
        return tuple(f)