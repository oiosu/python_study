# 아래 코드는 문자열을 입력받아 단어별로 나누는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# words = list(map(int, input().split()))
# print(words)

# ValueError: invalid literal for int() with base 10: 'python' 오류 발생

# 파이썬 형변환 에러 
# 문자형으로 바꿀 때는 str()
# 정수형으로 바꿀 때는 int()
# 실수형으로 바꿀 때는 float()

words = list(input().split())
# map 함수를 사용해서 int() 수정 

print(words)

# I'm Tutor 6
# ["I'm", 'Tutor', '6']