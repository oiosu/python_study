# 각 자릿수의 합 구하기 
# 정수 number가 주어질 때, 각 자릿수의 합을

number = 123
result = 0

while number:
    result += number%10
    number //= 10

print(result)