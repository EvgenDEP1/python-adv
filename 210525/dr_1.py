# дд.мм.гггг

date_n = {chr(el) for el in range(ord('0'), ord('9') + 1)}
date_n.update(['.'])

required_date = {'.'}
required_date_2 = {'.'}


def date_is_valid(date):
    date_as_set = set(date)
    if not date or date_as_set - date_n:
        return False

    for dot in required_date:
        check = date.count(dot)
        if check != 2:
            return False

    den, mes, god = date.split('.')
    if len(den) != 2 or len(mes) != 2 or len(god) != 4:
        return False
    return True


assert date_is_valid('01.02.2021')
assert not date_is_valid('12.232.20200')

print(date_is_valid('01.02.2021'))
print(date_is_valid('12.232.20200'))

