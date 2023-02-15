# batu kertas gunting

from random import randint

t = ["Batu", "Kertas", "Gunting"]

computer = t[randint(0,2)]
player = False
while player == False:
    player = input("Batu, Kertas, Gunting? :")
    if player == computer :
        print("Seri")
    elif player == "Batu":
        if computer == "Kertas":
            print("Menang")
            print("Kamu memilih :", player)
            print("Komputer memilih :", computer)
        else:
            print("Kalah")
            print("Kamu memilih :", player)
            print("Komputer memilih :", computer)
    elif player == "Kertas":
        if computer == " Gunting":
            print("Menang")
            print("Kamu memilih :", player)
            print("Komputer memilih :", computer)
        else:
            print("Kalah")
            print("Kamu memilih :", player)
            print("Komputer memilih :", computer)
    elif player == "Gunting":
        if computer == "Batu":
            print("Menang")
            print("Kamu memilih :", player)
            print("Komputer memilih :", computer)
        else:
            print("Kalah")
            print("Kamu memilih :", player)
            print("Komputer memilih :", computer)
    else:
        print("Kata yang anda masukan salah, silahkan cek lagi pengejaanya!")
    player == False
    computer == t[randint(0,2)]