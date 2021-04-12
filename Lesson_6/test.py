import datetime
import json

f = open('C:/acdc.json', 'r')
album = json.load(f)
album1 = dict(album)
a = album1.values()
a = dict(*a)
d = dict(a.get('tracks'))
p = (d.get('track'))
p = str(p)
p = p.split('ion\':')
elist = list()
for e in p:
    elist.append(e[2:5])
del elist[0]
print(elist)
lsum = sum([int(xs) for xs in elist])
print(lsum)
print(str(datetime.timedelta(seconds=lsum)))
