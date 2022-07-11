# 입력받은 숫자에 5을 더한 결과를 출력하시요.
num   = input()
print(num + 5)
# 다음과 같이 오류가 발생되는 이유는 input은 모두 strting으로 저장이 되기 때문이다. 아무리 숫자 형태라도
#   File "c:\Users\LGE\Desktop\Python\1day_python\codeup_6025.py", line 3, in <module>
# print(num + 5)
# 명시적 형변환을 해줘야한다. 
print(int(num))
# 따라서, 숫자로 활용하기 위해서는 항상 int 로 변환해야 한다. 