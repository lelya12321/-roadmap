# Строка состоит из символов [A-Za-z0-9 ].
# Написать метод, использующий re, который удаляет из строки все цифры.

import re

string__ = 'aaaSSSDG012SS44Vnn5'
g = re.sub(r'\d','', string__)
print(g)
