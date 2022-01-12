from time import time


def decorator(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        res = func(*args, **kwargs)
        t2 = time()
        print(t2-t1)
        return res
    return wrapper

@decorator
def a(n):
    return n**2
print(a(5))