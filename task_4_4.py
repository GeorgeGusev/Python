sp=[1, 2, 3, 4, 5]
s=5
for i in range(s):
    sp.append(sp.pop(0))
    print(sp)


sp1 = [0, 1, 2, 3, 4]
sp2 = []
i = 1
while i != len(sp1):
    sp2.insert(i, sp1[i])
    i += 1
sp2.insert(len(sp1), sp1[0])
print(sp2)