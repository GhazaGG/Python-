# latihan logika dan komparasi

# membuat gabungan rentang dari angka

# menggunakan variabel
print("++++++++3------------10+++++++++")
print(f"Masukan angka Kurang dari tiga\n atau lebih dari 10")
inputuser = float(input("Masukan angka!: "))

iskurangdari = inputuser < 3
print("Kurang dari 3 =",iskurangdari)

islebihdari = inputuser > 10
print("Lebih dari 10 =",islebihdari)

isCorrect = iskurangdari or islebihdari
print("angka yang anda masukan: ",isCorrect)

# Menggunakan function

# def gabunganAngka():
#     inputuser = float(input("Masukan Angkamu!"))
#     if inputuser <3 or inputuser >10:
#         print("true")
#     else:
#         print("false")


# gabunganAngka()



# Kasus irisan
# print("-----3++++++++10-----")


# menggunakan variabel
# print("Masukan angka lebih dari tiga\n dan tidak lebih dari 10")
# inputuser = float(input("masukan angka!"))
# islebihdari = inputuser > 3 
# print("Angka anda lebih dari 3: ",islebihdari)
# iskurangdari = inputuser < 10
# print("Angka anda kurang dari 10, ",iskurangdari)

# iscorrect = islebihdari and iskurangdari
# print("Angka anda benar:", iscorrect)


# menggunakan function
# def irisan():
#     inputuser = float(input("Masukan Angka: "))
#     if inputuser > 3 and inputuser < 10:
#         print("True")
#     else:
#         print("False")

# irisan()






# 1. ----- 0 ++++++++ 5 ---------- 8++++++++++11-------
# menggunakan function
# print("----- 0 ++++++++ 5 ---------- 8++++++++++11-------")
# def irisan1():
#     inputuser = float(input("Masukan Angka!: "))
#     if inputuser > 0 and inputuser < 5 or inputuser > 8 and inputuser < 11:
#         print("True")
#     else:
#         print("False")


# irisan1()

# 2. +++++ 0 -------- 5 ++++++++++ 8 ----------11++++++++

print(" +++++ 0 -------- 5 ++++++++++ 8 ----------11++++++++")
def irisan2():
    inputuser = float(input("Masukan Angka!"))
    if inputuser < 0 or inputuser > 5 and inputuser <8 or inputuser > 11:
        print("True")
    else:
        print("False")

irisan2()