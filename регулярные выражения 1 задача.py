# Написать функцию, которая возвращает
# длину самой длинной подстроки, которая состоит только из гласных (aiueoAIUEO).

import re
def max_len(string_):
    list_from_string = string_.split()
    list_2 = []
    for el in list_from_string:
        el_from_vowels = re.sub(r'[^aeiouAEIOU]', '', el)
        list_2.append(el_from_vowels)
    list_3 = []
    for a in list_from_string:
        for b in list_2:
            if a == b:
                list_3.append(b)

    print(max(list_3, key=len))
max_len('AV aa is eeei largest Uuuuiiioo Analytics community of')