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