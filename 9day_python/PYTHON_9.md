## ๐ Python_์์ฉ/์ฌํ

* **list Comprehension** 

: ํํ์๊ณผ ์ ์ด๋ฌธ์ ํตํด ํน์ ํ ๊ฐ์ ๊ฐ์ง ๋ฆฌ์คํธ๋ฅผ ๊ฐ๊ฒฐํ๊ฒ ์์ฑํ๋ ๋ฐฉ๋ฒ 

```python
[<expression> for <๋ณ์> in <iterable>]
[<expression> for <๋ณ์> in <iterable> if <์กฐ๊ฑด์>]
```

```python
#list comprehension

even_list = [i for i in range(10) if i % 2 == 0]
print(even_list)

even_list = [i**2 for i in range(10) if i % 2 == 0]
print(even_list)
```

```python
# 1~3์ ์ธ์ ๊ณฑ์ ๊ฒฐ๊ณผ๊ฐ ๋ด๊ธด ๋ฆฌ์คํธ ๋ง๋ค๊ธฐ 

cubic_list = []
for number in range(1, 4)     #์ด๋ถ๋ถ!
	cubic_list.append(number**3) 
print(cubic_list)

[number**3 for number in range(1, 4)] #์ฝ๋ ์ ์ดํด๋ณด๊ธฐ
```

---

* **Dictionary Comprehension**

: ํํ์๊ณผ ์ ์ด๋ฌธ์ ํตํด ํน์ ํ ๊ฐ์ ๊ฐ์ง ๋ฆฌ์คํธ๋ฅผ ๊ฐ๊ฒฐํ๊ฒ ์์ฑํ๋ ๋ฐฉ๋ฒ 

```python
{key: value for <๋ณ์> in < iterable > }  

{key: value for <๋ณ์> in < iterable> if <์กฐ๊ฑด์>}
```

```python
# 1~3์ ์ธ์ ๊ณฑ์ ๊ฒฐ๊ณผ๊ฐ ๋ด๊ธด ๋์๋๋ฆฌ ๋ง๋ค๊ธฐ 
cubic_dict = {}
for number in range(1, 4):
    cubic_dict[number] = number ** 3
print(cubic_dict)

{number: number**3 for number in range(1, 4)}
```

---



```python
# map(____, _____)
# map(int, input().split())
# int ํจ์๋ฅผ ์ ์ฉํ๋ ๊ฒ 
# map(ํจ์, ๋ฐ๋ณต๊ฐ๋ฅํ ๊ฒ)
# ๋ฐ๋ณต ๊ฐ๋ฅํ ๊ฒ๋ค์ ๋ชจ๋  ์์์ ํจ์๋ฅผ ์ ์ฉ์ํจ ๊ฒฐ๊ณผ๋ฅผ 
# map object๋ก ๋ฐํํ๋ค. 

#intํ ๋ณํํจ์๋ฅผ 
#input์ผ๋ก ๋ฐ์ ๊ฒ์ ์ชผ๊ฐ  ๊ฒฐ๊ณผ์ธ ๋ฆฌ์คํธ์ ๊ฐ๊ฐ ์ ์ฉํ๋ค. 

# ๊ธฐ๋ณธ ๋ฐ๋ณต / ์กฐ๊ฑด ์ฝ๋
numbers = [1, 2, 5, 10, 3, 9, 12]
result = []
for number in numbers:
    if numbers % 3 == 0:
        result.append(number*3)
print(result)     # [3, 6, 15, 30, 9, 27, 36]

# ๋ง์ฝ map์ผ๋ก ์ฌ์ฉํ๊ณ  ์ถ๋ค๋ฉด?
# (์ด ์ฝ๋๊ฐ ์ข๋ค๋ ๊ฒ์ ์๋)
# ์ฒซ๋ฒ์งธ๋ก ํจ์๋ฅผ ์ ์ํด์ผ ํ๋ค. 

def divided_by_3(number):
    return number * 3

print(list(map(multiple_3, numbers)))
# [3, 6, 15, 30, 9, 27, 36]

# ์ด ํจ์๋ ๊ณ์ ์ฌ์ฉ๋์ง ์๊ณ , map์์๋ง ์ฌ์ฉ๋๋ค. 
# ์์์ ์ธ ํจ์๋ฅผ ๋ง๋ค๊ณ  ์ถ๋ค. => lambda
# ๋๋ค ํ์ฉ
print(list(map(lambda n: n*3, numbers)))
# [3, 6, 15, 30, 9, 27, 36]
```



* **lambda [parameter] : ํํ์**

: ํํ์์ ๊ณ์ฐํ ๊ฒฐ๊ณผ๊ฐ์ ๋ฐํํ๋ ํจ์๋ก, ์ด๋ฆ์ด ์๋ ํจ์๋ผ์ ์ต๋ชํจ์๋ผ๊ณ ๋ ๋ถ๋ฆฐ๋ค. 

: return ๋ฌธ์ ๊ฐ์ง ์ ์๋ค. 

: ๊ฐํธ ์กฐ๊ฑด๋ฌธ ์ธ ์กฐ๊ฑด๋ฌธ์ด๋ ๋ฐ๋ณต๋ฌธ์ ๊ฐ์ง ์ ์๋ค. 

: ํจ์๋ฅผ ์ ์ํด์ ์ฌ์ฉํ๋ ๊ฒ๋ณด๋ค ๊ฐ๊ฒฐํ๊ฒ ์ฌ์ฉ์ด ๊ฐ๋ฅํ๋ฉฐ def๋ฅผ ์ฌ์ฉํ  ์ ์๋ ๊ณณ์ ์ฌ์ฉ ๊ฐ๋ฅํ๋ค.



๐ป **filter (functin, iterable)**

```
# ๊ธฐ๋ณธ ๋ฐ๋ณต / ์กฐ๊ฑด ์ฝ๋
numbers = [1, 2, 5, 10, 3, 9, 12]

result = []
for number in numbers:
    if numbers % 3 == 0:
        result.append(number*3)
print(result)     

print(filter(lambda n: n%3==0, numbers))
# filter object 

# ํจ์ ํ์ฉ
def is_3(n):
	if n % 3 == 0:
		return True
	else:
		return  False
		
#์์ ์ฝ๋์ ๊ฐ์ ์ฝ๋ 
return n5 3 == 0 #true, false ๋ถ๋ฆฐํ

# filter : ์ํ ๊ฐ๋ฅํ ๋ฐ์ดํฐ๊ตฌ์กฐ์ ๋ชจ๋  ์์์ ํจ์๋ฅผ ์ ์ฉํ๊ณ  ๊ทธ ๊ฒฐ๊ณผ๊ฐ true์ธ ๊ฒ๋ค์ filter objext๋ก ๋ฐํ 
# map(function, ___)
fuction : ๋ชจ๋  iterabble์๊ฒ ํจ์ ์ ์ฉํ๊ณ  
```

---

* **pip**

: ํ์ด์ฌ ํจํค๊ธฐ ๊ด๋ฆฌ์ 

: PyPI์ ์ ์ฅ๋ ์ธ๋ถ ํจํค์ง๋ค์ ์ค์นํ๋๋ก ๋์์ฃผ๋ ํจํค์ง ๊ด๋ฆฌ ์์คํ 

`pip install SomePackage`

`pip install SomePackage==1.0.5`

`pip install 'SomePackage>=1.0.4`

๐ ๋ชจ๋ bash, cmd ํ๊ฒฝ์์ ์ฌ์ฉ๋๋ ๋ช๋ น์ด!



* ํจํค์ง ์ญ์  : `pip uninstall SomePackage`

* ํจํค์ง ๋ชฉ๋ก ๋ฐ ํน์  ํจํค์ง ์ ๋ณด 

  : `pip list`

  : `pip show SomePackage`

* ํด๋นํ๋ ๋ชฉ๋ก์ requirements.txt๋ก ๋ง๋ค์ด ๊ด๋ฆฌํจ : `pip freeze`

* ํจํค์ง ๊ด๋ฆฌํ๊ธฐ

  : `pip freeze > requirements.txt`

  : `pip install -r requirements.txt`

---

* ๊ฐ์ํ๊ฒฝ 

  : ํ์ด์ฌ ํ์ค ๋ผ์ด๋ธ๋ฌ๋ฆฌ๊ฐ ์๋ ์ธ๋ถ ํจํค์ง์ ๋ชจ๋์ ์ฌ์ฉํ  ๊ฒฝ์ฐ ๋ชจ๋ pip๋ฅผ ํตํด ์ค์นํด์ผ ํ๋ค.

  : ๋ณต์์ ํ๋ก์ ํธ๋ฅผ ํ๋ ๊ฒฝ์ฐ ๋ฒ์ ์ด ์์ดํ  ์ ์์ผ๋ ์ฐธ๊ณ ํ  ๊ฒ!

  : ๊ฐ์ํ๊ฒฝ์ ๋ง๋ค์ด ํ๋ก์ ํธ๋ณ๋ก ๋๋ฆฝ์ ์ธ ํจํค์ง๋ฅผ ๊ด๋ฆฌํ  ์ ์๋ค. 



* **venv**

โ	: ๊ฐ์ํ๊ฒฝ์ ํฌํจํ๋ ๋๋ ํ ๋ฆฌ์ ์ด๋ฆ 

โ	: ๊ฐ์ํ๊ฒฝ ๋นํ์ฑํ : `$ deactivate` ๋ช๋ น์ด๋ฅผ ์ฌ์ฉ

* **python -m venv venv**

![image-20220721112430076](PYTHON_9.assets/image-20220721112430076.png)

![image-20220721112625473](PYTHON_9.assets/image-20220721112625473.png)

### **ํ๋ก์ ํธ ๋ง๋ค ํจํค์ง๋ผ๋ ๊ฑธ ๋ณ๋๋ก ๊ด๋ฆฌํ๊ธฐ ์ํด์**



![image-20220721115302346](PYTHON_9.assets/image-20220721115302346.png)

