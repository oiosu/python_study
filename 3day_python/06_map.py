numbers = ['1', '2', '3']

# 숫자로 바꿔서 쓰고 싶다? 
# 리스트를 숫자로 형 변환은 불가능하다. 
# 다만, 숫자 형태의 문자를 변환 할 수는 있다. 
# n = int(numbers)

#반복문! 
new_numbers =[]
for number in numbers:
    new_numbers.appen(int(number))
print(new_numbers)

# map!
numbers = ['1', '2', '3']
new_numbers_2 = map(int, numbers)
print(new_numbers_2)
print(list(new_numbers_2)) #리스트로 형변환해서 보면 바뀌어 있다.
# 보기 위해서 바꾼 것일 뿐 반드시 list로 바꿔야 하는 것은 아니다. 

