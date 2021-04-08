sdict = {'first_color': 'Red', 'second_color': 'Green', 'third_color': None}

for i in sdict.copy():
    if not sdict[i]:
        sdict.pop(i)

print(sdict)
