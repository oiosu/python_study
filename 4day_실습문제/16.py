# 모음 등장 여부 확인하기
# 문자열 word가 주어질 때, 해당 문자열에서 모음의 갯수를 출력하시오.
# 모음 : a, e, i, o, u 
# count() 사용 금지

a = ['a', 'e', 'i', 'o', 'u']
word = 'apple'
count = 0
for char in word:
    if char in a:
        count +=1
print(count)
