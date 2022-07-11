a = 5 #int
b = "5" #string
print(a, type(a))
print(b, type(b))

# 길이 len
fruit = "abcde"
print(len(fruit)) #5

# 접근 
print(fruit[1]) #b
# 컴퓨터에서는 숫자를 0부터

# 슬라이싱
print(fruit[1:3]) #bc
# index 1 이상, 3미만 
# a b c d e
# 0 1 2 3 4

# 마지막 값은?
# 파이썬은 음의 인텍스도 가지고 있다. 
print(fruit[len(fruit)-1])
print(fruit[-1])

# 심화응용
# s[::] 그대로
# s[::-1] 거꾸로