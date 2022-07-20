 

```python
# 클래스 정의
class Person:
    pass

# 인스턴스 생성
p1 = Person()
# 인스턴스 속성
p1.name = '홍길동'

print(p1.name)
```

 

```python
class Person:
    # 클래스 변수(속성)
    species = '사람'

    # 인스턴스 메서드
    # 인스턴스가 활용할 메서드
    def greeting(self):
        print('안녕하세요~!')

iu = Person()
iu.greeting()   #(): 메서드를 호출한 것 

# 클래스 변수(속성)
print(Person.species)    #species  : 메서드 이기 때문에 호출이 안된다.
```



![image-20220720233304961](PYTHON_8.assets/image-20220720233304961.png)



```python
#게임 예제

class Yasuo:

    def __init__(self):
        self.health = 100
        self.energy = 0


yasuo1 = Yasuo()
yasuo2 = Yasuo() 

yasuo1.health = yasuo1.health - 20

print(yasuo1.health, yasuo2.health)
```

---

### 😎 lotto

```python
import random 


for i in range(5):
    numbers = range(1, 46)
    result = random.sample(numbers, 6)
    result.sort() 
    print(result)

# numbers = range(1, 46)
# result = random.sample(numbers, 6)
# result.sort() 
# print(result)

# numbers = range(1, 46)
# result = random.sample(numbers, 6)
# result.sort() 
# print(result)

# numbers = range(1, 46)
# result = random.sample(numbers, 6)
# result.sort() 
# print(result)

# numbers = range(1, 46)
# result = random.sample(numbers, 6)
# result.sort() 
# print(result)
```



```python
import lotto_function

# 이 코드의 결과 
# 로또 번호들의 리스트
buy_numbers = lotto_function.generate_lotto(5)

lotto_function.check(buy_number, [1, 2, 3, 4, 5, 6])
```



```python
import lotto_class

lotto = lotto_class.Lotto()
lotto.generate_lotto()
print(lotto.numbers)
print(lotto.get_money([1, 2, 3, 4, 5, 6]))
```



```python
import random

class Lotto: 
    name = '로또추첨기'

    def generate_lotto(self):
        self.numbers = sorted(random.sample(range(1, 46), 6))

    def get_money(self, real_numbers):
        print('당신의 숫자는', self.numbers)
        print('당첨 숫자는', real_numbers)
        if self.numbers == real_numbers:
            return 10000000000
        else:
            return 0
```



```python
import random 


# n을 넣으면 
# 그 횟수만큼 
def generate_lotto(n):
    result = []
    for i in range(n):
        numbers = range(1, 46)
        pick = random.sample(numbers, 6)
        pick.sort()
        result.append(pick)
    return result

def check(buy_numbers, result_numbers):
    return 0

# print(generate_lotto(5))
```



---

### 🧐 메소드

```python
# 함수 내부에서 값을 쓰고 싶으면 어떻게 해야하죠?
# 정의할 때 이름을 지어놓고, 호출할 때 값을 넘겨줘요!

class MyClass:
    class_variable = '클래스변수'

    # 메서드들을 정의했습니다. 
    def __init__(self): 
        self.instance_variable = '인스턴스 변수'
    # 인스턴스 메서드 정의
    def instance_method(self):
        return self, self.instance_variable
    # 클래스 메서드 정의
    @classmethod
    def class_method(cls):
        return cls, cls.class_variable
    # 스태틱 메서드 정의
    @staticmethod
    def static_method():
        return '스태틱'

c1 = MyClass()
print('인스턴스 변수 호출', c1.instance_variable)
print('인스턴스 메서드 호출', c1.instance_method())
print('클래스 메서드 호출', c1.class_method())
print('스태틱 메서드 호출', c1.static_method())
```





---

### ✔ 클래스 속성 

: 한 클래스 모든 인스턴스라도 똑같은 값을 가지고 있는 속성 

: 클래스 선언 내부에서 정의 

: < classname > . < name > 으로 접근 및 할당 



* 인스턴스와 클래스 간의 이름 공간 (namespace)

: 클래스를 정의하면 클래스와 해당하는 이름 공간 생성 

: 인스턴스를 만들면 인스턴스 객체가 생성되고 이름 공간 생성 

: 인스턴스에서 특정 속성에 접근하면, 인스턴스-클래스 순으로 탐색 





### ✔ 크래스 메소드 

##### (클래스가 사용할 메소드)

@clssmethod 데코레이터를 사용하여 정의 

* 데코레이터: 함수를 어떤 함수로 꾸며서 새로운 기능을 부여 

호출 시, 첫번쨰 인자로 클래스(cls)가 전달됨 

```python
class MyClass

	@classmethod
	def class_method(cls, arg1, ...)
```



### ✔ 스태틱 메소드 

인스턴스 변수, 클래스 변수를 전혀 다루지 않는 메소드 

👉 언제 사용하나요?  : 속성을  다루지 않고 단지 기능(행동)만을 하는 메소드





```python
class MyClass:
	class_variable = '클래스 변수'
	
	#메서드를 정의 
	def __init__(self):
		self.insteance_variable = '인스턴스 변수'
 	#인스턴스 메서드
 	def instance_method(self):
 		return self, self.instance_variable
 
 	#클래스 메서드 
 	@classmethod
 	def class_method(cls):    #cls는 함수의 관용적 표현이 있을 뿐
 	return cls
 	#스태틱 정의
 	@staticmethod
 	def static_method():
 	return ''
 	
 
 
```

![image-20220720112903000](PYTHON_8.assets/image-20220720112903000.png)



---

**스태틱 메서드 안에서 클래스나 인스턴스를 쓸수 있을까요?  x**

**= 사용할 수 있는 방법은 전혀 없다.** 

**= input을 준 것만 내부적으로만 사용할 수 있지만 out으로는 no!!**

---





