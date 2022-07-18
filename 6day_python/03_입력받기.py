# 두 수를 Input으로 받아 합을 구하는 코드이다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.
# 10 20 / 30

# numbers = input().split()
# print(sum(numbers))

#TypeError: unsupported operand type(s) for +: 'int' and 'str' 오류 발생 
# int 타입을 str형과 + 연산자로 더할 수 없다는 오류 메시지 내용입니다. 
# 계산을 위해 양쪽 모두 숫자 int 이거나 문자 str이어야 한다. 

# 오류를 해결하기 위한 접근방식

numbers = input('숫자를 입력해주세요!: ')
print(int(numbers))
