xlist = 1, 2, 3, 4
# maxnumpos = 0
# maxnum = 0
# maxnumpos = 1
# maxnumpos
def maxn():
    m = 0
    for i in xlist:
        if i > xlist[m]:
            i = xlist[m]
            m = m + 1
        global maxnum
        maxnum = xlist[m]
        global maxnumpos
        maxnumpos = m


maxn()
print(maxnum)





