import exception
import func


def get_number():
    while True:
        number = input()
        if number.isdigit():
            return int(number)
        else:
            raise exception.MyException

def Process():
    while True:
        s = input("Знак (+,-,*,/): \n")
        if s == '0':
            break
        if s in ('+', '-', '*', '/'):
            print('Введите число')
            a = get_number()
            b = get_number()
            if s == '+':
                print('Ваше действие +')
                print(f'Ответ: {func.summa(a, b)}')
            elif s == '-':
                print('Ваше действие -')
                print(f'Ответ: {func.dif(a, b)}')
            elif s == '*':
                print('Ваше действие *')
                print(f'Ответ: {func.mul(a, b)}')
            elif s == '/':
                print('Ваше действие /')
                print(f'Ответ: {func.div(a, b)}')
        else:
            print('не верно выбран знак действия')