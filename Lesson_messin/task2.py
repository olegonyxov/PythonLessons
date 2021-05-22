import re

str1 = input(str("input phone number:"))
renew = "".join(re.findall(r'\d*\d+|\d+', str1))  # думаю, так намного полезней
print("{} {} {}-{}-{}".format("(+38)", renew[0:3], renew[3:6], renew[6:8], renew[8:10]))
