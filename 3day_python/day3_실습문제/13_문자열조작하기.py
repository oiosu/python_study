# 주어진 문자열 word가 주어질 때, 
# 해당 단어를 역순으로 뒤집은 결과를 출력
# apple

word = ('apple')
reversed_str = 'elppa'
for i in word:
    reversed = i + reversed_str

print(f'Original Word: {word}')
print(f'Reversed Word: {reversed_str}')