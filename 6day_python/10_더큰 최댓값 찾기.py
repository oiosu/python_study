# output: 두 번째 리스트의 최댓값이 더 큽니다.

number_list = [1, 23, 9, 6, 91, 59, 29]
max2 = max(number_list)

number_list2 = [2, 5, 100, 20, 50, 10, 91, 82]
max3 = max(number_list2)

if max2 > max3:
    print("첫 번째 리스트의 최댓값이 더 큽니다.")

elif max2 < max3:
    print("두 번째 리스트의 최댓값이 더 큽니다.")

else:
    print("첫 번째 리스트의 최댓값과 두 번째 리스트의 최댓값은 같습니다.")


# 변수 이름 수정하기 
# max = max(number_list) 해당 코드에서 변수를 max라는 예약어로 선언하여 max() 
# 내장함수 사용시 오류가 발생