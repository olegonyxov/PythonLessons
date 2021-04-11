def end_dict():
    l = 0
    edict = {}
    for u in coin:
        edict.update({coin[l]: code[l]})
        l = l + 1
    return edict

