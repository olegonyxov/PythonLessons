import random
string = 'somebody_email@gmail.com'
slices = string.split('@')
word1=slices[0]
word2=slices[1]

def change_char():
    i = random.randint(0, len(word1))
    a=0
    while a <3:
        word1.replace(word1[i],"*")
        a+=1

change_char()
print(word1)







