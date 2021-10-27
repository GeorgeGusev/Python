n=input('Введите четырехзначной число: ')
a=int(n[0])
b=int(n[1])
c=int(n[2])
d=int(n[3])
i=0
j=0
for i in n:
    i=a+b+c+d
for j in n:
    j=a*b*c*d

print(i,j)