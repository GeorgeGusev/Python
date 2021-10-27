x=int(input('Введите первой число: '))
sign=input('Введите знак +,-,/,*: ')
y=int(input('Введите второе число: '))
z=0

for z in x,y:
    if sign=='+':
        z=x+y
    if sign == '-':
        z=x-y
    if sign == '*':
        z=x*y
    if sign == '/':
        if y==0:
            z=('На ноль делить нельзя!')
        if y!=0:
            z=x/y
print(z)