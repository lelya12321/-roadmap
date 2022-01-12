
# Написать декоратор, выводящий в консоль входные параметры и возвращаемое значение функции.

def decorator(func):
    def wrapper(*args, **kwargs):
        res1 = func(*args, **kwargs)
        res2 = (*args,)
        print(res1, res2)

    return wrapper

@decorator
def function(a, b):
    return a+b

function(5, 10)