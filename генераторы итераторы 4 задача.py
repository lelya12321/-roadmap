# Написать генератор, возвращающий все возможные комбинации правильно вложенных скобок () фиксированной длины

from itertools import *

list_ = []
list_2 = []
for i in permutations('()()()'):
    list_.append(i)
set_1 = set(list_)
list_1 = list(set_1)
for i in list_1:
    new_val = ''.join(i)
    list_2.append(new_val)
list_3 = []
for el in list_2:
    if el.startswith(')'):
        pass
    else:
        list_3.append(el)

def function(string):
    result = 0
    for a in string:
        if "(" in a:
            result += 1
        if ")" in a:
            result -= 1
        if result < 0:
            pass
            break
    if result != 0:
        pass
    else:
        return string

gen_obj = map(function, list_3)
print(list(gen_obj))