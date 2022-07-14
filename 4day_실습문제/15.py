# 문자의 위치 구하기
# 문자열 word가 주어질 때, 해당 문자열에서 a 가 처음으로 등장하는 
# 위치(index)를 출력해주세요.
# a 가 없는 경우에는 -1을 출력해주세요.
# find() index() 메서드 사용 금지
# banana / 1

word = ('banana')
count = 0
result = -1

for i in word:
    if i == 'a':
        result = count
        break
    count += 1

print(result)

