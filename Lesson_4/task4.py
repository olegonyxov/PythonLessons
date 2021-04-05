n = int(input('input n:'))
nlist = range(1, n + 1, 1)
nnlist = str()
if n <= 9:
    for i in nlist:
        i = str(i)
        nnlist = nnlist.__add__(i)
        print(nnlist)
