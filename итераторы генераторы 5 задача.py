# Написать функцию prod, вычисляющую произведение всех
# чисел в итераторе (аналог sum, но для умножения вместо сложения), без использования циклов for и while.

from functools import reduce
def prod(iterable):
    return reduce(lambda x, y: x*y, iterable)