# 기본값이 sep는 ''으로 정의가 되어 있다.
print('hi', 'hohoho') # hi hohoho
# 키워드로 sep를 바꿔서 호출할 수 있다. 
print('ho', 'hohoho', sep='-') # ho-hohoho

print(1, 2, 3, 4, 5, 6, 7, 8)

#정해지지 않는 갯수의 인자 
def my_add(*numbers):
    # 내부적으로 numbers가 튜플
    return numbers

result = my_add(1, 2, 3)
print(result, type(result))

def my_func(**kwargs):
    return kwargs
result = my_func(name='su', age='199', gender='m') #딕셔너리
print(result, type(result))

