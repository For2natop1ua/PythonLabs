<h1 align="center">PythonLabs</h1>
<p align="center">
</p>

# Lab7
## Варіант 6
Напишіть програму на python, яка запитує у користувача 3 цілих числа і виводить на екран середнє арифметичне. Реалізувати обробку винятків.

### Lab7V6_1.py:
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
