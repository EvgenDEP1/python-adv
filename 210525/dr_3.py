import re


RE_NUMBERS_VALIDATOR = re.compile(r'^[0-9]+[.,][0-9]+$')


def numbers_is_valid(numbers):
    return RE_NUMBERS_VALIDATOR.match(numbers)


assert numbers_is_valid('1.32')
assert numbers_is_valid('1,32')
assert not numbers_is_valid(',')

print(numbers_is_valid('1.32'))
print(numbers_is_valid('1,32'))
print(numbers_is_valid(','))
