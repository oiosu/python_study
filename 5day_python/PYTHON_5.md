# ๐ฅ PYTHON_POJECT

### 1. ๋ชจ๋

* ๋ค์ํ ๊ธฐ๋ฅ์ ํ๋์ ํ์ผ๋ก (๋ชจ๋)

* ๋ค์ํ ํ์ผ์ ํ๋์ ํด๋๋ก (ํจํค์ง)

* ๋ค์ํ ํจํค์ง๋ฅผ ํ๋์ ๋ฌถ์์ผ๋ก (๋ผ์ด๋ธ๋ฌ๋ฆฌ) ์ด๊ฒ์ ๊ด๋ฆฌํ๋ ๊ด๋ฆฌ์ (PIP)

---

๐ **๋ชจ๋ : ํน์  ๊ธฐ๋ฅ์ ํ๋ ์ฝ๋๋ฅผ ํ์ด์ฌ ํ์ผ ๋จ์๋ก ์์ฑํ ๊ฒ** 

๐ **ํ์ด์ฌ ํ์ค ๋ผ์ด๋ธ๋ฌ๋ฆฌ : ํ์ด์ฌ์ ๊ธฐ๋ณธ์ ์ผ๋ก ์ค์น๋ ๋ชจ๋๊ณผ ๋ด์ฅ ํจ์** 

---

```python
import datetime #import : (๋ชจ๋์)๊ฐ์ง๊ณ  ์ค๋ค.

now = datetime.datetime123.now()
print(now, type(now))

#์ ์ฝ๋์ ๋์ผํ๋ค. 
from datetime import datetime123
now = datetime.now()
```

---

#### 1๏ธโฃ **random.sampe(population, k, * counts=none)**

* ํจ์์์ ์ค์ํ๊ฑด, input๊ณผ output์ด๋ค. 
* **point** ๊ณ ์ ํ ์์์ k ๊ธธ์ด ๋ฆฌ์คํธ๋ฅผ ๋ฐํํด์ค๋๋ค. 

```python
#lotto

import random
#1~46๊น์ง์ ์ซ์ !
# ๊ทธ์ค์ 6๊ฐ 
numbers = random.sample(range(1, 46,) 6)
numbers.sort() #์ ๋ ฌ
print(numbers, type(numbers)) #type์ list

#5๋ฒ์ ๋๋ค lotto ๋ฒํธ 
n = int(input('์ผ๋ง์ธ๋? '))
for i in range(n):
    numbers = random.sample(range(1, 46,) 6)
	numbers.sort() 
	print(numbers, type(numbers))
```

---

* #### with : ๊ฐ์ฒด๋ฅผ ๋ค๋ฃฐ ๋ with ํค์๋๋ฅผ ์ฌ์ฉํ๋ ๊ฒ์ ์ข์ ์ต๊ด์ด๋ค. 

with ํํ์ ๋์ค ์์ธ๊ฐ ๋ฐ์ํ๋๋ผ๋ ์ค์ํธ๊ฐ ์ข๋ฃ ๋  ๋ ์ฌ๋ฐ๋ฅด๊ฒ ๋ซํ๋ค๋ ๊ฒ 

๋ง์ฝ, with๋ฅผ ์ฌ์ฉํ์ง ์๋๋ค๋ฉด, f.close()๋ฅผ ํธ์ถํ์ฌ ์ฌ์ฉ๋ ์์คํ์ ์ฆ์ ๋ฐ๋ฉ

```python
# file.py

with open('test.txt', 'w', encoding='utf-8') as f:
    f.write('Hello Su!\n') #\n (๊ฐํ_์ค๋ฐ๊ฟ)๊ผญ ํด์ค์ผํจ 
    for i in range(1, 6):
    	f.write(f'{i} ๋ฒ์งธ!\n') #\n (๊ฐํ_์ค๋ฐ๊ฟ)๊ผญ ํด์ค์ผํจ 
```

`w ์ฐ๊ธฐ ์ ์ฉ = ๋ฎ์ด์`

`a append ์ฐ๋๋ฐ ํ์ผ ์์ผ๋ฉด ์ด์ด์ ์`

`r ์ฝ๊ธฐ ์ ์ฉ`



---

```python
# students.txt ๋ฅผ read
# read.py

# ํ์ผ๋ช, ์ด๋ค ๋ชจ๋๋ก ์ด์ง,
# ์ธ์ฝ๋ฉ์ ์ค์ 
with open('students.txt', 'r', encoding='utf-8')as f: #f๋ ํ์ผ๋ช
	# ํ์คํธ๋ stringํ์
    text = f.read()
    print(text, type(text))
    # string.split() ๋ listํ์
    names = text.split()
    cnt = 0
    for name in names:
        # name: ์ฒซ๋ฒ์งธ ์ํ  - ๊น 00 # ๊น์จ์ธ ์ฌ๋์ธ ์๋ฅผ ๊ตฌํ์์ค. 
        # ์ธ์ ? ๊น์จ?
       # if name.startswith('๊น') : => ์ฒซ๋ฒ์งธ ๋ฐฉ๋ฒ
        if name[0] == '๊น':       # => ๋๋ฒ์งธ ๋ฐฉ๋ฒ
            cnt += 1
        print(cnt)

```

---

```python
with open('students.txt', 'r', encoding='utf-8') as f:
	lines = f.readline() #ํ์ค์ฉ ๋ถ๋ฌ์ค๋ ๊ฒ 
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

lines = f.readline()  #ํ์ค์ฉ ์ฝ์ด์ค
print(lines, type(lines))

# ๋ง์ฝ ์ค์ ๋ชจ๋ ์ฝ์ผ๋ ค๋ฉด ๋ฐ๋ณต๋ฌธ ์ฌ์ฉํ๊ธฐ
for line in f:
    print(line, end="")

```

```python
lines = f.readlines()
print(lines, type(lines))
# ์ถ๋ ฅ ์ ๋ฆฌ์คํธ ํ์ 
# /n ์ด ๋ถ์ฌ์ ์ถ๋ ฅ๋จ
```

---

#### { } ๋์๋๋ฆฌ [ ] ๋ฆฌ์คํธ

### 2. json

```python
#json.py
import json

#ํ์ผ์ ์ด๊ณ , 
f = open('stocks.json', 'r', endcoding='utf-8')
#json์ ํ์ด์ฌ ๊ฐ์ฒด ํ์์ผ๋ก ํ๋ค!
kospi = json.load(f)
#samsung = kospi['stocks'][0] 
#print(samsung, type(samsung))
print(kospi['stocks'][0]) #stocks๋ฅผ ํ์ ๋ list ์ด๋ค. 

# stockname ์ ๋ณด๋, cloeprice ์ ๋ณด๋ง ๊ฐ์ง ๋์๋๋ฆฌ๋ฅผ ๋ง๋ค๊ณ  ์ถ๋ค. 
result = {
    'stockName':samsung.get('stockName'),
    'closePrice':samsung.get('closePrice')
}
print(result)

```

```python
from pprint import pprint #๋์๋๋ฆฌ ์ด์๊ฒ ๋ณผ ์ ์๋๋ก ํ๋ ๊ฒ 
```

