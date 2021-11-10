def double_fact(n: int) -> int:
    if n % 2 == 0:
        list = [n for n in range(1, n+1) if n % 2 == 0]
    else:
        list = [n for n in range(1, n+1) if n % 2 != 0]
    result = 1
    for i in list:
        result *= i
    print(f'Результат двойного факториала для {n} = {result}')


def main():
    print('Введите 5 чисел: ')
    count = 0
    tmp = []
    while count != 5:
        num = int(input())
        tmp.append(num)
        count += 1
    for i in tmp:
        double_fact(i)


if __name__ == '__main__':
    main()