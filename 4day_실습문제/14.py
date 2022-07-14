# 문제 14. 문자의 갯수 구하기
# 문자열 word가 주어질 때, 해당 문자열에서 a 개수를 구하세요.
# count() 메서드 사용 금지
# apple / 1

# 만약 count()메서드를 사용하게 된다면 다음과 같이 코드를 작성할 수 있습니다. 
# result = 'apple'
# print(result.count('a'))


word = ('aplle')
count = 0

for i in word:
    if i == 'a':
        count += 1
    
print(count)

