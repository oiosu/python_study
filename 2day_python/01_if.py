#1.num은 input으로 사용자에게 입력을 받으세요.

num =int(input())

print(num, type(num)) #반드시 실행시키는 연습하기

#2. 조건문을 통해서 홀수/짝수 여부를 출력하세요.
# 숫자로서의 num! / 타입이 무엇인지 확인할 필요가 있다
if num % 2 == 1:
    print('홀수')
else:
    print('짝수')