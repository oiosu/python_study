# 주어진 리스트 numbers에서 최솟값을 구하여 출력하시오.
# min() 함수 사용 금지
# input : numbers = [0, 20, 100]
# ouput : 0

#min()함수로 이용하여 최댓값을 구해본다면, 
#print(min(0, 20, 100)) 이렇게 쉽게 구할 수 있겠지만, for문을 사용하여 최솟값을 구해본다면 다음과 같다. 


numbers = (0, 20, 100)
result =0
for i in ():
    if result == 0 or  i < result:
        result = i 
print(result)