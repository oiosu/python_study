#1부터 n까지의 곱을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.
# input : n = 5
# output : 120

#while
n = int(input())
result = 1
i = 1
while i <= n:
    result *= i
    i += 1
print(result)

#for
n = int(input())
result = 1
for j in range(n):
    j +=1
    result *= j
print(result)
