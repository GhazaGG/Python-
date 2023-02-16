MAX_LINE = 3


def deposit():
    while True:
        jumlah = input ("Masukan jumlah yang akan anda deposit: ")
        if jumlah.isdigit():
            jumlah = int(jumlah)
            break
        else:
            print("Masukan nilai yang benar!")
    return jumlah

def line():
    while True:
        line = input ("Masukan jumlah baris yang anda bet! : ( 1-"+ str(MAX_LINE)+ ")?")
        if line.isdigit():
            line = int(line)
            if 1 <= line <= MAX_LINE:
                break
            else:
                print("Tolong masukan jumlah yang benar")
        else:
            print("Tolong masukan jumlah yang benar!")
    return line 


saldo = deposit()
line = line()
print("Jumlah saldo anda: ", saldo)
print("Line yang anda bet", line)


