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
