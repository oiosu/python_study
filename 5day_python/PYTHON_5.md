# 🔥 PYTHON_POJECT

### 1. 모듈

* 다양한 기능을 하나의 파일로 (모듈)

* 다양한 파일을 하나의 폴더로 (패키지)

* 다양한 패키지를 하나의 묶음으로 (라이브러리) 이것을 관리하는 관리자 (PIP)

---

👉 **모듈 : 특정 기능을 하는 코드를 파이썬 파일 단위로 작성한 것** 

👉 **파이썬 표준 라이브러리 : 파이썬에 기본적으로 설치된 모듈과 내장 함수** 

---

```python
import datetime #import : (모듈을)가지고 오다.

now = datetime.datetime123.now()
print(now, type(now))

#위 코드와 동일하다. 
from datetime import datetime123
now = datetime.now()
```

---

#### 1️⃣ **random.sampe(population, k, * counts=none)**

* 함수에서 중요한건, input과 output이다. 
* **point** 고유한 요소의 k 길이 리스트를 반환해줍니다. 

```python
#lotto

import random
#1~46까지의 숫자 !
# 그중에 6개 
numbers = random.sample(range(1, 46,) 6)
numbers.sort() #정렬
print(numbers, type(numbers)) #type은 list

#5번의 랜덤 lotto 번호 
n = int(input('얼마쓸래? '))
for i in range(n):
    numbers = random.sample(range(1, 46,) 6)
	numbers.sort() 
	print(numbers, type(numbers))
```

---

* #### with : 객체를 다룰 때 with 키워드를 사용하는 것은 좋은 습관이다. 

with 혜택은 도중 예외가 발생하더라도 스위트가 종료 될 때 올바르게 닫힌다는 것 

만약, with를 사용하지 않는다면, f.close()를 호출하여 사용된 시스템을 즉시 반납

```python
# file.py

with open('test.txt', 'w', encoding='utf-8') as f:
    f.write('Hello Su!\n') #\n (개행_줄바꿈)꼭 해줘야함 
    for i in range(1, 6):
    	f.write(f'{i} 번째!\n') #\n (개행_줄바꿈)꼭 해줘야함 
```

`w 쓰기 전용 = 덮어씀`

`a append 쓰는데 파일 있으면 이어서 씀`

`r 읽기 전용`



---

```python
# students.txt 를 read
# read.py

# 파일명, 어떤 모드로 열지,
# 인코딩을 설정
with open('students.txt', 'r', encoding='utf-8')as f: #f는 파일명
	# 텍스트는 string타입
    text = f.read()
    print(text, type(text))
    # string.split() 는 list타입
    names = text.split()
    cnt = 0
    for name in names:
        # name: 첫번째 시행  - 김 00 # 김씨인 사람인 수를 구하시오. 
        # 언제? 김씨?
       # if name.startswith('김') : => 첫번째 방법
        if name[0] == '김':       # => 두번째 방법
            cnt += 1
        print(cnt)

```

---

```python
with open('students.txt', 'r', encoding='utf-8') as f:
	lines = f.readline() #한줄씩 불러오는 것 
	print(lines, type(lines))
```

```python
with open('students.txt', 'r', encoding='utf-8') as f:
	for line in f:
		print(line, end='')
```

---

```python
readline()

lines = f.readline()  #한줄씩 읽어줌
print(lines, type(lines))

# 만약 줄을 모두 읽으려면 반복문 사용하기
for line in f:
    print(line, end="")

```

```python
lines = f.readlines()
print(lines, type(lines))
# 출력 시 리스트 타입 
# /n 이 붙여서 출력됨
```

---

#### { } 딕셔너리 [ ] 리스트

### 2. json

```python
#json.py
import json

#파일을 열고, 
f = open('stocks.json', 'r', endcoding='utf-8')
#json을 파이썬 객체 형식으로 한다!
kospi = json.load(f)
#samsung = kospi['stocks'][0] 
#print(samsung, type(samsung))
print(kospi['stocks'][0]) #stocks를 했을 때 list 이다. 

# stockname 정보랑, cloeprice 정보만 가진 딕셔너리를 만들고 싶다. 
result = {
    'stockName':samsung.get('stockName'),
    'closePrice':samsung.get('closePrice')
}
print(result)

```

```python
from pprint import pprint #딕셔너리 이쁘게 볼 수 있도록 하는 것 
```

