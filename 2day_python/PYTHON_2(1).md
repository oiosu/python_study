# π» PYTHON_κΈ°μ΄1 

### π 1. μ‘°κ±΄λ¬Έ 

>  μ°Έ κ±°μ§μ νλ¨ν  μ μλ μ‘°κ±΄μκ³Ό ν¨κ» μ¬μ©

* **κΈ°λ³Ένμ** 

```python
if < expression : 

	#run thins code block

else:

	`#run thins code block`
```

* **μμ ** 

```python
a = -10

	if a >=0:

		print('μμ')

	else:

		print('μμ')

print(a)
```



* **μμ ** 

```python
a = 10

if a>= 0:

print('μμ')

else:

print('μμ')

print(a)
```



* **μμ ** 

```python
num =int(input())

print(num, type(num))

if num % 2 == 1:

 	 print('νμ')

 else:

 	print('μ§μ') 
```



* **TypeError**

![image-20220712093232274](PYTHON_2.assets/image-20220712093232274.png)

<span style="color:blue">TypeError λνλ μ΄μ  : μ«μλ‘μμ num (νμ νμΈνκΈ° λ¬Έμμ΄μΈμ§, μ«μμΈμ§)</span>



---



### βΌ  λ³΅μ μ‘°κ±΄λ¬Έ 

> λ³΅μμ μ‘°κ±΄μμ νμ©ν  κ²½μ°elifλ₯Ό νμ©νμ¬ νννλ€. 

```python
if expression :
	#code block

elif expression:
	#code block

elif expression
	#code block
```



---



###  βΌ μ€μ²© μ‘°κ±΄λ¬Έ 

>  μ‘°κ±΄λ¬Έμ λ€λ₯Έ μ‘°κ±΄λ¬Έμ μ€μ²©λμ΄ μ¬μ©λ  μ μμ

```python
if expression : 
	#code block
	if expression : 
		# code block
else: 
	#code block
```





* **μ€μ΅ λ¬Έμ  ( λ μ½λ λΉκ΅νλ©΄μ μκ°ν΄λ³΄κΈ°)**

```python
 dust = 1000
 
 if dust > 150:
 	print('λ§€μ° λμ¨')
 elif dust > 80:
 	print)('λμ¨')
 elif dust > 30:
 	print('λ³΄ν΅')
 elif: 
 	if dust < 0 
    	print('μμ κ°μλλ€.')
    else:
        print('μ’μ')
```

```python
dust = -10

if dust > 150:
    print('λ§€μ° λμ¨')
elif dust > 80:
    print('λμ¨')
elif dust > 30: 
    print('λ³΄ν΅')
elif dust > 0:
    print('μ’μ')
else: 
    print('μμ κ°μλλ€.')
```



**π <span style="color:red">λ¨κ³μ μΌλ‘ μ½λκ° μ΄λ»κ² μ€ννλμ§ μμμλΆν° νμ€ νμ€μ© μ΄ν΄λ³΄λκ²μ΄ μ€μν¨!</span>**



---

###  βΌ μ‘°κ±΄ ννμ 

>  μ‘°κ±΄ ννμ conditional expression 

`μμλ‘ λ°κΎΈλ μ½λ ` `value = num if num >= 0 else -num`

`num μ°ΈμΌ κ²½μ° `

`num >= 0 expression`

`-num κ±°μ§μΌ κ²½μ° `





