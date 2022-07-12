#주어진 숫자의 평균을 구하는 코드를 작성하시오.
#sum(), len()  함수 사용 금지
#input : numbers = [3, 10, 20]
#output : 11


numbers = [3, 10, 20]

result = 0
for val in numbers: 
    result += val
print(f"averrage: {result / len(numbers)}")
