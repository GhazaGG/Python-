#  program sederhana untuk mengganti huruf vokal pada suatu kata atau kalimat


teks = input("Masukan kata atau kalimat yang ingin anda ganti: ")
pengganti = input("Masukan huruf pengganti: ")

def menggantiHurufVokal(kalimat, pengganti):
    vokal = "aiueoAIUEO"
    for huruf in vokal:
        kalimat = kalimat.replace(huruf, pengganti)
    return kalimat

print("Kalimat yang anda masukan adalah: ", teks)
print("kata yang anda masukan adalah: ", pengganti)
print("Hasil dari pergantian: ", menggantiHurufVokal(teks, pengganti))



