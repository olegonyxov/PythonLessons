inp_temp = float(input('temp:'))
inp_scale = str(input('scale:'))
if inp_scale == 'K':
    K = int(inp_temp)
    C = K - 273.5
    F = K * 1.8 - 459.67
if inp_scale == "C":
    C = int(inp_temp)
    K = C + 273.5
    F = K * 1.8 - 459.67
if inp_scale == "F":
    F = int(inp_temp)
    K = (F + 459.67) / 1.8
    C = K - 273.5
print('Цельсий:', int(C), 'Фарингейт:', int(F), 'Кельвин:', int(K))
