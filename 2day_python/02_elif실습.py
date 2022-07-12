dust = 100

# dust가 150 보다 크면, 매우 나쁨 
if dust > 150:
    print('매우 나쁨')
# 80보다 크면, 나쁨
elif dust > 80:
    print('나쁨')
# 30보다 크면, 보통
elif dust > 30:
    print('보통')
# 좋은
# else는 위의 모든 조건에 해당하지 않는 나머지의 경우이기에 별도의 조건은 불가능
# else는 조건문에서 생략이 가능하다. 
else:
    print('좋음')

#실수1_elif 쓰다보니 else에도 '조건'추가한다.