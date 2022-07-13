sum = 5
print(sum([1, 2, 3]))

#Traceback (most recent call last):
  #File "c:\Users\LGE\Desktop\Python\3day_python\05_LEGB.py", line 2, in <module>
    #print(sum([1, 2, 3]))
#TypeError: 'int' object is not callable

# sum 이 지금은 5가 되버림 
# built-in scope에 sum 함수가 있었음 
# global scope에 sum 이름의 변수를 만듬 
# 제가 찾으니깐 L E G B