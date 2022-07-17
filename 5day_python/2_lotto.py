#lotto

import random
#1~46까지의 숫자 !
# 그중에 6개 
numbers = random.sample(range(1, 46,) 6)
numbers.sort() #정렬
print(numbers, type(numbers)) #type은 list

#5번의 랜덤 lotto 번호 
n = int(input('얼마쓸래? '))
for i in range(n):
    numbers = random.sample(range(1, 46,) 6)
	numbers.sort() 
	print(numbers, type(numbers))