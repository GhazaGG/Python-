
# program sederhana untuk pengecekan ganjil/genap sebuah bilangan

def modulus():
    a = int(input("Masukan nilai/angka :"))
    if a % 2 == 0:
        print("Genap")
    else:
        print("Ganjil")

modulus()