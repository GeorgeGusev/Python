n = int(input('Введите целое число: '))
s = 1
if n == 1:
    print('Сумма равна', s)
else:
    for i in range(2, n+1):
        s = s + 1/i
    print(s)