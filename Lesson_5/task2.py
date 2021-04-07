xstr = input('input some text:')
xstr2 = xstr.split()
n = 0
for i in xstr2:
    n += 1
print('количество слов :', n)
print('общее количество символов, включая пробелы:', len(xstr))
print('общее количество символов без пробелов:', len(xstr) - xstr.count(' '))
