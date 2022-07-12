# 🔻 PYTHON_기초1 

### 📂 3.  FOR

> for 반복 가능한 객체를 모두 순회하면 종료 (별도의 종료문이 없음)

> for문은 시퀀스 를 포함한 순회가능한 객체 요소를 모두 순회함 

>  처음부터 끝까지 모두 순회하므로 별도의 종료 조건이 필요하지 않음 

```python
for < 변수명 > in < interable >:

	#code block
```



* 문자열 순회 

: 사용자가 입력한 문자를 한 글자씩 세로로 출력하시오. 

```python
for chars in charse:
    	print(char) 
```

> h
>
> i

: range를 활용하여 한 글자씩 출력하시요. (index로 접근하여 사용하기)

```python
for index in range(len(char)):

	print(char[index])
```

> index를 기준으로 순회를 한다. 

---

### 📂 4.  딕셔너리 순회

> 딕셔너리는 기본적으로 key를 순회하여, key를 통해 값을 활용 

---

### 📂 5.   반복문 제어

* brak
  * 반복문 종료 
* continue
  * contune이후의 코드 블록은 수행하지 않고, 다음 반복을 수행
* for-else
  * 끝까지 반복문을 실행한 이후에 else문 실행
  * break를 통해 중간에 종료되는 경우 else 문은 실행 되지 않음

