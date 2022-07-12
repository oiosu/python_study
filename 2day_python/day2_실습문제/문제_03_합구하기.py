# 1부터 n까지의 합을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.
# n = 10
# 55

# while 

a = 0
n = 10
result = 0

while a < n:
    a += 1
    result += a

print(result)


# for

n = 10
result = 0

for i in range(1, n+1):
    result += i
    
print(result)
