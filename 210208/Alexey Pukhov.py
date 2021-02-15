import random

file_name = "some_csv.csv"

lines = open(file_name).read().split(',')
myline = random.choice(lines)
print(myline)

# Алексей не смог запушить из-за того что забыл пароль от гита и ушёл на WorldSkills,
# # поэтому попросил меня его работу у себя запушить.
