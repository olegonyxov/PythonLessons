xl = input('input some list:')
alist = xl.split(',')

def k_v():
    x=0
    sdict= {}
    for i in alist:
        sdict.update({alist.index(alist[x]):alist[x]})
        x= x+1
    return sdict

print(k_v())
