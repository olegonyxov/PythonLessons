import datetime
import json

result = list()
with open('C:/acdc.json', 'r') as f1:
    allalbum = json.load(f1)
    print(f1.read())
    for i in allalbum['album']['tracks']['track']:
        result.append(i['duration'])
sumres = sum([int(xs) for xs in result])
print(sumres)
print(str(datetime.timedelta(seconds=sumres)))
