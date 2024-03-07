import random 
class TebakAngka:
    def __init__(self, nama):
        self.nama = nama
        self.angka = random.randint(1, 10)
        self.percobaan = 0

    def intro(self):
        print(f"Selamat datang {self.nama}! silahkan tebak angka yang sudah dari 1-10")

    def Tebak(self, angka):
        self.percobaan += 1
        if angka == self.angka:
            print(f"Selamat, {self.nama} menebak dengan benar dengan {self.percobaan} percobaan !")
            return True
        else:
            print("Tebakan salah. Coba lagi !")
            return False

    def __del__(self):
        print(f"Game tebak angka selesai. Total percobaan: {self.percobaan}")

def validasi(func):
    def pengecekan(self, angka):
        if 1 <= angka <= 10:
            return func(self, angka)
        else :
            print("Masukkan tebakan antara 1 sampai 10.")
            return False

    return pengecekan

TebakAngka.Tebak = validasi(TebakAngka.Tebak)

nama = str(input("Harap masukkan nama : "))
game = TebakAngka(nama)
game.intro()

while True:
    angka = int(input("Masukkan tebakan Anda (1-10) : "))
    if game.Tebak(angka):
        break
