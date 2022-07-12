# 주어진 리스트 numbers에서 두번째로 큰 수를 구하여 출력하시오.
# max() 함수 사용 금지
# numbers = [0, 20, 100]
# output: 20


numbers = [0, 20, 100]
result = set(numbers)
sorted(result, reverse=True)[1]
print(numbers[1])