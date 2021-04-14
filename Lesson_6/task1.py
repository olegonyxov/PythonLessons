def end_dict():
    l = 0
    edict = {}
    for u in coin:
        edict[coin[l]]= code[l]
        l += 1
    return edict
