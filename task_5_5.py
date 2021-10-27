from random import randint as rint
mas = []
for i in range(0, 19):
    mas.append(rint(0, 100))
print(mas)
max_n = max(mas)
print(max_n)
for i in range(len(mas)):
    if mas[i] % 2 == 0:
        mas[i] = max_n
print(mas)