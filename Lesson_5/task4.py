import random
i=0
nlist = list(range(1,random.randint(0,100)))
n1list = []

for i in nlist:
    if int(i) % 2 == 0:
        n1list.append(i)
    else:
        n1list.append(0)



print(nlist)
print(n1list)
print(n1list.count(0))
