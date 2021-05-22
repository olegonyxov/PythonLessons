import re
str1 = "aaaaaaaaaSASA31213"
str = "dasdasdASDASD12312$#@-+="
str=re.findall(r"\S+",str)
str=re.findall(r"\S+\D+",str[0])
str=re.findall(r"\S+\D+\W+",str[0])
print(str)