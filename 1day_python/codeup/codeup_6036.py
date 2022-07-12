# 단어와 반복 횟수를 입력받아 여러 번 출력
# 문자열 * 정수 또는 정수 * 문자열은 그 문자열을 여러 번 반복한 문자열을 만들어 준다.
# love 3
# lovelovelove

w, n = input().split()
n=int(n)
print(w*n)