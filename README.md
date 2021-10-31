<h1 align="center">PythonLabs</h1>
<p align="center">
</p>

# Lab6
## Варіант 6
Напишіть програму, яка створює файл із N випадковими цілими парними числами.

### Lab6V6_1.py:
```python
import random


def createFile(myFile, q):
    with open(myFile, "w") as outFile:
        outFile.writelines(["{}\n".format(x) for x in random.sample(range(0, 101, 2), q)])


n = int(input("Введіть скільки випадкових цілих парних чисел треба записати у файл\n"))
createFile("foo.txt", n)
```
---
