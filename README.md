<h1 align="center">PythonLabs</h1>
<p align="center">
</p>

# Lab1
## Варіант 6
Напишіть програму на python, яка запитує у користувача слово, число і після цього виводить введене слово введене число раз. Приклад виведення:
>  Ви ввели слово: ку  
> Слово після перетворення 4 рази: кукукуку
```python
print("Введіть слово:", end=" ")
text = input()
print("Скільки разів повторювати це слово:", end=" ")
num = int(input())
print("Ви ввели слово: {0}".format(text))
print("Слово після перетворення {0} рази: {1}".format(num, text * num))

```
---

# Lab2
## Варіант 6
Напишіть програму на python, яка запитує у користувача 3 цілих числа і
виводить на екран середнє арифметичне. Використовувати функцію.
```python
def avg(first, second, third):
    s = (first + second + third) / 3
    return s


a = int(input("Введіть перше ціле число:"))
b = int(input("Введіть друге ціле число:"))
c = int(input("Введіть третє ціле число:"))

avg = round(avg(a, b, c), 2)

print("({}+{}+{})/3 = {} - середнє арифметичне".format(a, b, c, avg))

```
---

# Lab3
## Варіант 6
### 6.1
Напишіть програму на python, яка запитує у користувача позитивне
число a - сторону трикутника, а також 2 прилеглих кута A і B в градусах. Обчислити
площу трикутника і вивести на екран. У задачі використовувати модуль з функцією для
обчислень. Приклад виведення:
> Ви ввели сторону a: 300, кут A: 30, кут B: 40  
> Площа: ...

#### Lab3V6_1.py:
```python
import AreaTriangle as at

side = int(input("Введіть сторону трикутника:"))
if side <= 0:
    print("Сторона трикутника не може бути менша або дорівнювати 0!")
else:
    f_angle = int(input("Введіть перший кут:"))
    s_angle = int(input("Введіть другий кут:"))
    if f_angle | s_angle < 0:
        print("Кути трикутника не можуть бути від'ємними!")
    else:
        a = at.area(side, f_angle, s_angle)
        print("Ви ввели сторону a: {}, кут A: {}, кут B: {}".format(side, f_angle, s_angle))
        print("Площа трикутника: {}".format(round(a, 2)))
```
#### AreaTriangle.py:
```python
import math


def area(side, alpha, beta):
    alpha = math.radians(alpha)
    beta = math.radians(beta)
    return math.pow(side, 2) / 2 * ((math.sin(alpha) * math.sin(beta)) / math.sin(math.pi - (alpha + beta)))
```
### 6.2
Дан одновимірний масив з 10 чисел. Запросити у користувача число і вивести всі
елементи масиву, які більше введеного.
```python
s = int(input("Введіть число від 0 до 9:"))
if s > 9 or s < 0:
    print("Невірно введене число.")
else:
    for i in range(10):
        if i > s:
            print(i)
```
---
