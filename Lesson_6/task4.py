import json
import datetime
from nested_lookup import nested_lookup

with open('C:/acdc.json', 'r') as f:
    album = json.load(f)
    results = nested_lookup(key='duration', document=album, wild=True)
    sumres = sum([int(xs) for xs in results])
print(sumres)
print(str(datetime.timedelta(seconds=sumres)))
