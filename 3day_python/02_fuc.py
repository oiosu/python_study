def foo():
    return 1, 2 # (1, 2 class tuple)

result = foo()
print(result, type(result))

def no():
    a = 1

result = no()
print(result, type(result)) #none class none type

# print g함수는 
# 출력을 해주고, return 값은 없습니다. none
a = print('hi')
print(a, type(a)) # none calss nonetype

a = 'hi'
print(a)

