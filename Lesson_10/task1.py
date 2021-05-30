def writetofile():  # ради практики- в тхт
    with open('C:\\tr1\\polid.txt', 'w', encoding='utf-8') as file1:
        i_string = str
        while i_string != "":
            i_string = input("input some string:")
            if i_string != "":
                file1.write(i_string), file1.write("\n")
        print("strings added to file")


if __name__ == "__main__":
    writetofile()
