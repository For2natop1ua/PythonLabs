<h1 align="center">PythonLabs</h1>
<p align="center">
</p>

# Lab4
## Варіант 6
Дано двовимірний масив випадкових чисел MxM. Обчислити визначник (детермінант)
матриці.

#### Lab3V6_1.py:
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