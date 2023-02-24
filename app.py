import random


secretNumber = random.randint(1, 100)

numberGuessing = 5

while numberGuessing > 0:
    guess = int(input("Masukan Tebakanmu!:"))
    numberGuessing -= 1
    if secretNumber == guess:
        print("Selamat anda benar!")
        break
    elif secretNumber > guess:
        print("Tebakan anda kurang tinggi!")
    else:
        print("Tebakan anda terlalu tinggi!")

    print(f"Sisa kesempatan anda adlah: {numberGuessing}")

if numberGuessing == 0:
    print("Sisa kesempatan anda telah habis")