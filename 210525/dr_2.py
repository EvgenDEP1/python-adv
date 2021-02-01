numbers = {chr(el) for el in range(ord('0'), ord('9') + 1)}
numbers.update(['.', ','])

required_symbol = {'.'}


def numbers_is_valid(number):
    numbers_as_set = set(number)
    if not number or numbers_as_set - numbers:
        return False

    for tochka in required_symbol:
        check = number.count(tochka)
        if check != 1:
            return False

    do, posle = number.split('.')
    if len(do) < 1 or len(posle) < 1:
        return False
    return True


assert numbers_is_valid('1.32')
assert not numbers_is_valid('1')

print(numbers_is_valid('1.32'))
print(numbers_is_valid('.'))
