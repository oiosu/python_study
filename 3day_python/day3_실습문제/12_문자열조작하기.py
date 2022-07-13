# 주어진 문자열 word가 주어질 때, 
# 해당 단어에서 ‘a’를 모두 제거한 결과를 출력
# apple

word = ('apple')
word_1 = ('a')

word = ''.join(x for x in word if x not in word_1)
print(word)