from random import randint as rint
n=int(input('Введите число n: '))
m=int(input('Введите число m: '))
i=0
maxls=[]
diag=[]
matr=[[rint(0,20) for x in range (m)] for y in range(n)]
print(matr)
for y in matr:
     maxls.append(max(y))
print(maxls)
for y in matr:
    for x in matr:
       if i in range(len(matr)):
           diag.append(x[i])
       i+=1
print(diag)
i=0
for y in matr:
    for x in matr:
       if i in range(len(matr)):
          x[i]=maxls[i]
       i+=1

print(matr)