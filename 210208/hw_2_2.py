import random
import re


# RE_PROVERKA = re.compile(r'\b[А-ЯЁ]?[а-яё]{2,}\b')
RE_PROVERKA = re.compile(r'\b[А-ЯЁ]?[а-яё]+\b')

# RE_PROVERKA = re.compile(r'[^а-яА-Я ]')
f = open('text.txt', 'r', encoding='utf-8')
text = f.read()
# text = RE_PROVERKA.sub('', text)
print(text)
bad_chars = [';', ':', '?', '.', ',', '!', '~', '\n', '…', '-']

for i in bad_chars:
    text = text.replace(i, ' ')
text = text.split(" ")

slova_ru = [w for w in filter(RE_PROVERKA.match, text)]
print(slova_ru, '\n')

i = 0
# ip = int(input('Введите количество рандомных слов: '))
while i != 10:
    i += 1
    print(i, random.choice(slova_ru))

f.close()
