import re

str1 = input(str("input phone number:"))
# some = re.findall(r'\d*\d+|\d+', str1)
renew = "".join(re.findall(r'\d*\d+|\d+', str1))
print(renew)
print("(+380)", renew[0:3], renew[3:6], "-", renew[6:8], "-", renew[8:10])
