dict1 = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
dict2 = {}
for i in dict1.keys():
    k = str(len(i))
    k2 = i+k
    v = dict1.get(i)
    dict2[k2] = v
dict1 = dict2
print(dict1)



dict1 = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
dict2 = {}

k = list(dict1.keys())
v = list(dict1.values())
dict1.clear()
i = 0
while i != len(k):
    dict1[k[i]+str(len(k[i]))] = v[i]
    i += 1
print(dict1)