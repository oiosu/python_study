# 아래 코드는 1부터 N까지의 숫자에 2를 곱해서 변수에 저장하는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.
# output : [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


# N = 10
# answer = ()
# for number in range(N + 1):
#     answer.append(number * 2) #!!!!!!!!!!!!!!!!!!오류 발생부분
# print(answer)

# AttributeError: 'tuple' object has no attribute 'append' 오류 발생
# 해결방법 
# 소괄호 ( )로 이루어진 튜플은 값 수정이나 삭제, 추가를 할 수 없습니다. 
# 따라서 append로 값을 추가하려면 대괄호 [ ] 로 리스트를 만들어야 합니다. 

N = 10
answer = []  #대괄호로 수정
for number in range(N + 1):
    answer.append(number * 2)

print(answer)

# 출력 올바르게 나옴 
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]