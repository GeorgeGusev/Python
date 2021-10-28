m = int(input('Нижнее значение: '))
n = int(input('Верхнее значение: '))

for i in range(m, n+1):
    spisok=[]
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            spisok.append(str(j))
    print('{}:{}'.format(i, ' '.join(spisok)))