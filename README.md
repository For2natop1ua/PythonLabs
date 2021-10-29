<h1 align="center">PythonLabs</h1>
<p align="center">
</p>

# Lab5
## Варіант 6
Написати мовою Python 4 класи, які імітують наступну модель
успадкування. Розширити класи властивостями та методами на власний розсуд. Створити
екземпляри класу та вивести інформацію про кожен об'єкт.

![Image alt](https://github.com/For2natop1ua/PythonLabs/raw/Lab5_Variant6/screen.png)




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
