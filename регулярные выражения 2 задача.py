# Написать регулярное выражение для проверки строки на соответствие любому из следующих форматов (вместо x может быть цифра 0-9).
# +7xxxxxxxxxx
# +7 (xxx) xxx-xx-xx
# +7 xxx xxx xxxx

import re

number_ = '+79525620102'
d = re.fullmatch(r'[+7]{2}[0-9]{10}', number_)
number_2 = '+7 952 562-01-02'
e = re.fullmatch(r'[+7]{2}\s[0-9]{3}\s[0-9]{3}-[0-9]{2}-[0-9]{2}', number_2)
number_3 = '+7 952 562 0102'
f = re.fullmatch(r'[+7]{2}\s[0-9]{3}\s[0-9]{3}\s[0-9]{4}', number_3)
print(bool(d), bool(e), bool(f))
