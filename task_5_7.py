from random import randint as rint
import numpy

n = int(input('Ввести размер матрицы: '))
matrix = numpy.rint(1, 100, size=(n, n))
print('Старая матрица: ', matrix)
for i in range(n):
    matrix[i][i] = max(matrix[i])
print('Новая матрица: ', matrix)