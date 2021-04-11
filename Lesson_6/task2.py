import time

def countdown(ntime):
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    return ntime


@countdown
def ntime():
    print(time.strftime('%H:%M'))


ntime()
