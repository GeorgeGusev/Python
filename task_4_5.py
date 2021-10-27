f1=0
f2=1
n=int(15)

print(f1, f2, end=' ')

for i in range(2, n):
    f1, f2=f2, f1 + f2
    print(f2, end = ' ')

fib=[]
m=0
while m != n:
    if m == 0 or m == 1:
        fib.append(1)
    else:
        last = fib[m - 1]
        prev_last = fib[m - 2]
        fib.append(last + prev_last)
    m += 1
print(fib)