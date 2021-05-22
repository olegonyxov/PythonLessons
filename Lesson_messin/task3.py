import re

if re.search(r"\w[a-z]", istring)[0]:
    if re.search(r"\w[A-Z]", istring)[0]:
        if re.search(r"\d", istring)[0]:
            if re.search(r"\W", istring)[0]:
                if len(str)>8:
                    print("password acceptable")
if __name__ == "__main__":
    istring = input(str("Input your password:"))

    # istring = "dasdasdASDASD12312$#@-+="
