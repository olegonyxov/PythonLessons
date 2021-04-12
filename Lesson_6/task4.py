import json
from datetime import datetime

f = open('C:/acdc.json', 'r')
album = json.load(f)
album1 = dict(album)
a = album1.values()
a = dict(*a)
d = dict(a.get('tracks'))
p = (d.get('track'))
p=str(p)
p=p.split('ion\':')
x=0
elist=list()
for e in p:
    elist.append(e[2:5])
    x=x+1
del elist[0]
print(elist)
lsum=sum([int(xs) for xs in elist])
print(lsum)

