sp=[2,33,44,57,22,153]
n=0
for i in sp:
    if i%2==0:
        n+=1
print('Количество четных чисел:', n)



sp1=[2,34,44,57,22,152]
len_sp1 = len(sp1)
i = 0
m=0
while i != len_sp1:
    if sp1[i] % 2 == 0:
        m +=1
    i +=1
print('Количество четных чисел:', m)