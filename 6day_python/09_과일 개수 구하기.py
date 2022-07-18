from pprint import pprint

fruits = [
    "Soursop",
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",
    "Salal berry",
]

fruit_count = {}

for fruit in fruits:
    if fruit not in fruit_count:
       fruit_count[fruit] = 1   #fruit_count[fruit] = 1 를 통해 딕셔너리에 추가하는 코드
    else:
        fruit_count[fruit] += 1

pprint(fruit_count)


# {'Apricot': 1,
#  'Blackcurrant': 1,
#  'Cantaloupe': 1,
#  'Feijoa': 1,
#  'Grapefruit': 1,
#  'Juniper berry': 1,
#  'Salal berry': 1,
#  'Soursop': 1}