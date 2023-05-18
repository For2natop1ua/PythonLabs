<h1 align="center">PythonLabs</h1>
<p align="center">
</p>

# Lab1
## Варіант 6
Напишіть програму на python, яка запитує у користувача слово, число і після цього виводить введене слово введене число раз. Приклад виведення:
>  Ви ввели слово: ку  
> Слово після перетворення 4 рази: кукукуку
#### Lab1V6.py:
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
#### Lab2V6.py:
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


# Lab6
## Варіант 6
Напишіть програму, яка створює файл із N випадковими цілими парними числами.

### Lab6V6.py:
```python
import random


def createFile(myFile, q):
    with open(myFile, "w") as outFile:
        outFile.writelines(["{}\n".format(x) for x in random.sample(range(0, 101, 2), q)])


n = int(input("Введіть скільки випадкових цілих парних чисел треба записати у файл\n"))
createFile("foo.txt", n)
```
---


# Lab7
## Варіант 6
Напишіть програму на python, яка запитує у користувача 3 цілих числа і виводить на екран середнє арифметичне. Реалізувати обробку винятків.

### Lab7V6.py:
```python
def avg(sum):
    return (sum) / 3


sum = 0

try:
    for i in range(1, 4):
        s = int(input("Введіть {} ціле число:\n".format(i)))
        sum += s

except ValueError as e1:
    print("Помилка! Введіть коректне ціле число! ({})".format(e1))
else:
    print("Середнє арифметичне: {}".format(round(avg(sum), 2)))

```
---


# Lab8
Встановити PyCharm, створити файл та запустити просту програму “Hello, World!”.

#### main.py:
```python
print("Hello, world!")
```
---


# Lab9
## Варіант 6
Напишіть програму на python з графічним інтерфейсом, яка запитує у користувача 3 цілих числа. Додати кнопку "Порахувати". Після натискання на кнопку
"Порахувати" на екрані в полі "Результат" виводиться середнє арифметичне.
Використовувати модуль TKinter.
### main.py:
```python
from tkinter import *


def display_avg():
    result_entry.delete(0, END)
    result_entry.insert(0, round(((first.get() + second.get() + third.get()) / 3), 2))


root = Tk()
root.title("Лабораторна робота №9")

first = IntVar()
second = IntVar()
third = IntVar()
result = IntVar()

first_label = Label(text="a:")
second_label = Label(text="b:")
third_label = Label(text="c:")
result_label = Label(text="Результат:")

first_label.grid(row=0, column=0, sticky="w")
second_label.grid(row=1, column=0, sticky="w")
third_label.grid(row=2, column=0, sticky="w")
result_label.grid(row=3, column=0, sticky="w")

first_entry = Entry(textvariable=first)
second_entry = Entry(textvariable=second)
third_entry = Entry(textvariable=third)
result_entry = Entry(textvariable=result)

first_entry.grid(row=0, column=1, padx=5, pady=5)
second_entry.grid(row=1, column=1, padx=5, pady=5)
third_entry.grid(row=2, column=1, padx=5, pady=5)
result_entry.grid(row=3, column=1, padx=5, pady=5)

message_button = Button(text="Порахувати", command=display_avg)
message_button.grid(row=4, column=1, padx=5, pady=5, sticky="e")

first_entry.delete(0, END)
second_entry.delete(0, END)
third_entry.delete(0, END)
result_entry.delete(0, END)

root.mainloop()
```
---


# Lab10
## Варіант 6
Напишіть програму на python, макет якої представлений нижче. При натисканні на
кнопку “Перемістити”, зелене коло переміщається з лівого кута до правого. При цьому 4
рази змінює свій колір, як показано на малюнку. Використовувати модуль Tkinter.

[![screen.png](https://i.postimg.cc/159ZSqX7/screen.png)](https://postimg.cc/V5HhB5jX)

### Lab10V6.py:
```python
import itertools
from tkinter import *

root = Tk()
root.title("Лабораторна робота №10")
root.geometry("800x500")
canvas = Canvas(root, width=800, height=500, bg='white')
color_iteration = itertools.cycle(('green', 'yellow', 'blue', 'black', 'lime'))


def move():
    global direction
    if canvas.coords(circle)[0] >= 700 or canvas.coords(circle)[0] <= 0:
        direction = -direction
    if canvas.coords(circle)[0] == 150 or canvas.coords(circle)[0] == 350\
            or canvas.coords(circle)[0] == 475 or canvas.coords(circle)[0] == 650:
        canvas.itemconfig(circle, fill=next(color_iteration), outline=next(color_iteration))
    canvas.move(circle, direction, 0)
    root.after(10, move)


btn_move = Button(text="Перемістити", command=move)
btn_move.pack()
canvas.pack()

direction = 5
circle = canvas.create_oval(10, 10, 60, 60, fill=next(color_iteration), outline=next(color_iteration))

root.mainloop()
```
---


# Lab11-12
Написати програму на python + PyQt5 на допомогу медичним працівникам.
Користувач програми  повинен мати можливість завантажити з диска DICOM файл.
Програма має відобразити на екрані вміст цього файлу у вигляді зображення.

### main.py:
```python
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from main_form import Ui_MainWindow
import matplotlib.pyplot as plt
from pydicom import dcmread
import sys
from PyQt5.QtWidgets import QMessageBox


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionupload_file.triggered.connect(self.btn_convert_clicked)

    def btn_convert_clicked(self):
        try:
            fname = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "DICOM files (*.dcm)")
            fn = fname[0]
            ds = dcmread(fn)
            arr = ds.pixel_array
            plt.imshow(arr, cmap="gray")
            plt.show()
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Помилка!")
            msg.setInformativeText('Під час завантаження файлу сталася помилка.')
            msg.setWindowTitle("Помилка")
            msg.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    my_window = MainWindow()
    my_window.show()
    sys.exit(app.exec())
```
### main_form.py:
```python
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 416, 21))
        self.menubar.setObjectName("menubar")
        self.menumenu = QtWidgets.QMenu(self.menubar)
        self.menumenu.setObjectName("menumenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionupload_file = QtWidgets.QAction(MainWindow)
        self.actionupload_file.setObjectName("actionupload_file")
        self.menumenu.addAction(self.actionupload_file)
        self.menubar.addAction(self.menumenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DICOM Viewer"))
        self.menumenu.setTitle(_translate("MainWindow", "Меню"))
        self.actionupload_file.setText(_translate("MainWindow", "Завантажити файл"))
```
---
