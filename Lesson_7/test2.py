zline = ('str(''2021-04-20', '  :::: ', 10.16, '   ', 8.98)
zline = str(zline)
crap = [')','(',',','\'']
print(zline)
zline.translate(None,"')''(")
print(zline)

