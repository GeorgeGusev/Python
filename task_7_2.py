while True:
    var = int(input('1. Длина\n' '2. Вес\n' '3. Объем\n' '0. Выход\n'
                    'Введите порядковый номер конвертируемого раздела: '))

    if var == 0:
        break

    if var  == 1:
        print('Конвертация длины.')

        length = int(input('Что считаем?\n'
                        '1. Дюймы в сантиметры\n' '2. Сантиметры в дюймы\n'
                        '3. Мили в километры\n' '4. Километры в мили\n'
                        '0. Выход\n'
                        'Введите конвертируемую длину: '))
        if length == 1:
            inch = float(input('Сколько дюймов? '))
            print(inch, 'дюймов равно', round((inch*2.54), 2),'сантиметров')
        elif length == 2:
            cm = float(input('Сколько сантиметров? '))
            print(cm, 'сантиметров равно', round((cm * 0.393701), 2), 'дюймов')
        elif length == 3:
            mile = float(input('Сколько миль? '))
            print(mile, 'миль равно', round((mile * 1.60934), 2), 'километров')
        elif length == 4:
            km = float(input('Сколько километров? '))
            print(km, 'километров равно', round((km * 0.621371), 2), 'миль')
        elif length == 0:
                break

    if var == 2:
        print('Конвертация веса.')
        massa = int(input('Что считаем?\n'
                        '1. Фунты в килограммы\n' '2. Килограммы в фунты\n' 
                         '3. Унции в граммы\n' '4. Граммы в унции\n' '0. Выход\n'
                         'Введите конвертируемый вес: '))
        if massa == 1:
            lb = float(input('Сколько фунтов? '))
            print(lb, 'фунтов равно', round((lb * 0.453592), 2), 'килограммов')
        elif massa == 2:
           kg = float(input('Сколько килограммов? '))
           print(kg, 'килограммов равно', round((kg * 2.20462), 2), 'фунтов')
        elif massa == 3:
            ounce = float(input('Сколько унций? '))
            print(ounce, 'унций равно', round((ounce * 28.3495), 2), 'граммов')
        elif massa == 4:
            gr = float(input('Сколько граммов? '))
            print(gr, 'граммов равно', round((gr * 0.035274), 2), 'унций')
        elif massa == 0:
            break

    if var == 3:
        print('Конвертация объема.')
        volume = int(input('Что считаем?\n'
                        '1. Галлон в литры\n' '2. Литры в галлоны\n'
                        '3. Пинты в литры\n' '4. Литры в пинты\n' '0. Выход\n'
                        'Введите конвертируемый объем: '))
        if volume == 1:
            gallon = float(input('Сколько галлонов? '))
            print(gallon, 'галлонов равно', round((gallon * 3.78541), 2), 'литров')
        elif volume == 2:
            liter = float(input('Сколько литров? '))
            print(liter, 'литров равно', round((liter * 0.264172), 2), 'галлонов')
        elif volume == 3:
            pint = float(input('Сколько пинтов? '))
            print(pint, 'пинтов равно', round((pint * 0.473176), 2), 'литров')
        elif volume == 4:
            liter_1 = float(input('Сколько литров? '))
            print(liter_1, 'литров равно', round((liter_1 * 2.11338), 2), 'пинтов')
        elif volume == 0:
                break