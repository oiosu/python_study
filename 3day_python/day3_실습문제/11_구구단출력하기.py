#2단부터 9단까지 반복하여 구구단을 출력
#문자열 출력시 f-string을 활용하면 편하게 작성

for x in range (2, 10):
    for y in range (1, 10):
        print(x, '*', y, '=', x * y)
        if (y == 9):
            print('----------')