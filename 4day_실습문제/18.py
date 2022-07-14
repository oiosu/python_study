# 알파벳 등장 갯수 구하기
# 문자열 word가 주어질 때, Dictionary를 활용해서 
# 해당 문자열에서 등장한 모든 알파벳 개수를 구해서 출력하세요.
# banana
# b 1
# a 3
# n 2

word = 'banana'
dict = {}

for i in word:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

for k,v in dict.items():
    print(k, v)