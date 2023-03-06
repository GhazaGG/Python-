# Program sederhana untuk aplikasi toko atau kasir
# kurang nota pembelian

nama = input("Masukan nama anda: ")
pesanan =[]
totalBill = 0

# daftar harga
mieAyam = 15000
Bakso = 10000
esTeh = 5000
kentangGoreng = 5000




def menu():
    global totalBill
    print("-"*5,"Menu","-"*5)
    print(f" 1. Mie ayam Rp {mieAyam:,}\n 2. Bakso Rp{Bakso:,}\n 3. Es Teh Rp {esTeh:,}\n 4. Kentang Goreng{kentangGoreng:,}")
    order = int(input("Pilih menu: "))
    if order == 1:
        jumlah = int(input("Masukan Jumlah pesanan Mie ayam: "))
        billMie = jumlah * mieAyam
        totalBill += billMie
        pesanan.append(f"Mie Ayam x{jumlah}")
        confirmpesanan()
    elif order == 2:
        jumlah = int(input("Masukan Jumlah pesanan Bakso ayam: "))
        billBakso = jumlah * Bakso
        totalBill += billBakso
        pesanan.append(f"Bakso x{jumlah}")
        confirmpesanan()
    elif order == 3:
        jumlah = int(input("Masukan Jumlah pesanan Es Teh: "))
        billTeh = jumlah * esTeh
        totalBill += billTeh
        pesanan.append(f"Esteh x{jumlah}")
        confirmpesanan()
    elif order == 4:
        jumlah = int(input("Masukan Jumlah pesanan Kentang Goreng: "))
        billKentang = jumlah * kentangGoreng
        totalBill += billKentang
        pesanan.append(f"Kentang Goreng x{jumlah}")
        confirmpesanan()
    else:
        confirmpesanan()

def diskon():
    global totalBill
    konfirmasiDiskon = input("Apakah anda memiliki kode diskon? (Y/N)")
    if konfirmasiDiskon == "Y":
        kode = input("Masukan Kode diskon: ")
        if kode == "diskon10":
            print(f"Selamat anda mendapatkan potongan harga sebesar 10%")
            print(f"Total belanjaan anda adalah {totalBill}")
            hargaDiskon = (10/100)*totalBill
            print(f"Total belan anda dipotong diskon 10% menjadi: {hargaDiskon}")
            totalBill -= hargaDiskon
        elif kode == "diskon20":
            print("Selamat anda mendapatkan potongan harga sebesar 20%")
            hargaDiskon = (20/100)*totalBill
            totalBill -= hargaDiskon
        else:
            print("Kode yang anda masukan salah")
    elif konfirmasiDiskon == "N" or konfirmasiDiskon == "n":
        print("Terimakasih")
    else:
        print("Terimakasih")

def confirmpesanan():
    confirm = input("Apakah ada yang ingin anda pesan lagi?: (Y/N) ")
    if confirm == "Y" or confirm == "y":
        menu()
    elif confirm == "N" or confirm == "n":
        print("Terimakasih")
        diskon()
    else:
        print("invalid code")
        confirmpesanan()

menu()

