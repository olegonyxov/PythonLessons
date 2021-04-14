import datetime
import json

from nested_lookup import nested_lookup

f = open('C:/acdc.json', 'r')
album = json.load(f)
results = nested_lookup(key='duration', document=album, wild=True)
sumres = sum([int(xs) for xs in results])
print(sumres)
print(str(datetime.timedelta(seconds=sumres)))
