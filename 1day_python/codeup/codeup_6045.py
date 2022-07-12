# 정수 3개를 입력받아 합과 평균을 출력
# 합과 평균을 공백을 두고 출력한다.
# 평균은 소숫점 이하 셋째 자리에서 반올림하여 둘째 자리까지 출력

a, b, c = input().split()
a=int(a)
b=int(b)
c=int(c)
hap=a+b+c
avg=hap/3
print(hap, format(avg, ".2f"))