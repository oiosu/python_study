a = '1, 2, 3'
# print(a.split())
# 문자열을 특정 단위로 쪼개줌!
# 리스트!
# ['1', '2', '3']

#numbers = a.split()
#result = int(numbers[0]) = int(numbers[1]) + int(numbers[2])
#print(result)

a = '10:20'
numbers = a.split(':')
print(numbers) #['10', '20']
# 출력할 때 sep(seperator)를 작성하면 값 사이에 해당 문자를 넣어서 출력!
print(numbers[0], numbers[1], sep='****') #10****20
