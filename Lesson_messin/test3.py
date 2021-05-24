import re
istring = "dasdasdASDASD12312$#@-+="
a =re.search(r"\W", istring)
print(a)