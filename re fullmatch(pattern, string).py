# НЕ используя библиотеку re, напишите функцию fullmatch(pattern, string)
# для проверки строки string на соответствие шаблону pattern.


def ffullmatch(string, pattern):
    if type(string) and type(pattern) != str:
        print('TypeError')
    else:
        for i in range(len(string)+1):
            if pattern[i] == '*':
                b = i - 1
                z = string.count(pattern[b])
                if z >=0:
                    while string[b] == pattern[b]:
                        str_from_string = string.replace(string[b], '')
                        break
                    str_from_pattern = pattern.replace('*', '').replace(pattern[b], '')

                    print(str_from_string==str_from_pattern)


            elif pattern[i] == '+':
                b = i - 1
                z = string.count(pattern[b])
                if z >=1:
                    while string[b] == pattern[b]:
                        str_from_string = string.replace(string[b], '')
                        break
                    str_from_pattern = pattern.replace('+', '').replace(pattern[b], '')
                    print(str_from_string == str_from_pattern)

            elif pattern[i] == '?':
                b = i - 1
                z = string.count(pattern[b])
                if z <=1:
                    while string[b] == pattern[b]:
                        str_from_string = string.replace(string[b], '')
                        break
                    str_from_pattern = pattern.replace('?', '').replace(pattern[b], '')
                    print(str_from_string == str_from_pattern)


ffullmatch('aValidString122343', "aValidString12*343")