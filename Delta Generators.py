def func(values, n):
    gen_object = (values[-i - 1] - values[-i - 2] for i in range(len(values) - 1))
    res = list(reversed(list(gen_object)))

    if n == 1:
        return res
    else:
        s = 0
        while s < n-1:
            s += 1
            new_gen = (res[-i - 1] - res[-i - 2] for i in range(len(res) - 1))
            res = list(reversed(list(new_gen)))
        return res