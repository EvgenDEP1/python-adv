file_name = "text.txt"

# print(*lines)

bad_chars = [';', ':', '!', "*", " "]
#
# from random import choice
#
# lines = (line for line in open(file_name, 'r', encoding='utf-8'))
#
#
# def mygen(n: int):
#     for i in range(n):
#         yield choice(lines.split())
#
#
# lst = mygen(3)
# print(*lst)














# line = lines.join(i for i in line if not i in bad_chars)


# print(*lines)
# lines = (s.strip(',').split(" ") for s in lines)




def Gem():
    lines = (line for line in open(file_name, 'r', encoding='utf-8'))
    for i in bad_chars:
        lines = lines.replace(i, ' ')
    print(*lines)


print(Gem())




# lines = (line for line in open(file_name, 'r', encoding='utf-8'))
# print(*lines)

# lines = ''.join(i for i in lines if not i in bad_chars)
#
# print(*lines)
# lines = (s.strip().split(" ") for s in lines)
# print(list_line)
#
# cols = next(list_line)
# cols = next(list_line)
#
# print(*list_line)



