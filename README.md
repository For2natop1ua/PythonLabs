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
#### Lab3V6_2.py:
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


# Lab4
## Варіант 6
Дано двовимірний масив випадкових чисел MxM. Обчислити визначник (детермінант)
матриці.

#### Lab4V6.py:
```python
import random

import numpy as np


def print_matrix(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end=' ')
        print()


print("Введіть значення М: ")
m = int(input())
arr = []
for i in range(m):
    arr.append([random.randrange(9) for i in range(m)])
det_arr = round(np.linalg.det(arr), 3)
print("Матриця МхМ:")
print_matrix(arr)
print('Детермінант матриці= {}'.format(det_arr))

```

# Lab5
## Варіант 6
Написати мовою Python 4 класи, які імітують наступну модель
успадкування. Розширити класи властивостями та методами на власний розсуд. Створити
екземпляри класу та вивести інформацію про кожен об'єкт.

[![screen.png](https://i.postimg.cc/fW883t5r/screen.png)](https://postimg.cc/xqbvhdwv)




### Registration.py:
```python
class Registration:
    id = None
    date = None
    name = None
    phone = None

    def __init__(self, id, date, name, phone):
        self.id = id
        self.date = date
        self.name = name
        self.phone = phone

    def print_info(self):
        print("id = {0}\ndate = {1}\nname = {2}\nphone = {3}".format(self.id, self.date, self.name, self.phone))

    def print_info_qr(self):
        print("name = {0}\nphone = {1}".format(self.name, self.phone))

```
### QuickReg.py:
```python
import Registration as reg


class QuickReg(reg.Registration):

    def __init__(self, id, date, name, phone):
        super().__init__(id, date, name, phone)

    def print_info(self):
        print("------Quick Registration------")
        super().print_info_qr()

```
### WebReg.py:
```python
import Registration as reg


class WebReg(reg.Registration):
    browser = None
    ipAddress = None

    def __init__(self, id, date, name, phone, browser, ipAddress):
        super().__init__(id, date, name, phone)
        self.browser = browser
        self.ipAddress = ipAddress

    def print_info(self):
        print("------Web Registration------")
        super().print_info()
        print("Browser: {0}\nIP_address: {1}".format(self.browser, self.ipAddress))

```
### DesktopReg.py:
```python
import Registration as reg


class DesktopReg(reg.Registration):
    administrator = None

    def __init__(self, id, date, name, phone, administrator):
        super().__init__(id, date, name, phone)
        self.administrator = administrator

    def print_info(self):
        print("------Desktop Registration------")
        super().print_info()
        print("Administrator: {}".format(self.administrator))

```
### main.py:
```python
import Registration as reg
import DesktopReg as dr
import WebReg as wr
import QuickReg as qr

registration = reg.Registration("1", "22.10.2021", "Abraham Lincoln", "387-835-6447")
desktopReg = dr.DesktopReg("2", "22.10.2021", "Jason Statham", "+1-289-524-4535", "Vin Diesel")
webReg = wr.WebReg("3", "23.10.2021", "Paul Walker", "+1-289-524-4535", "Google Chrome", "31.223.56.122")
quickReg = qr.QuickReg("", "", "Johnny Silverhand", "1-958-943-2355")

registration.print_info()
desktopReg.print_info()
webReg.print_info()
quickReg.print_info()
```
---
