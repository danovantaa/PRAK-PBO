class Dagangan:
    sum = 0
    list_barang = []

    def __init__(self, name, stock, value):
        self.name = name
        self.stock = stock
        self.value = value

        Dagangan.sum += 1
        Dagangan.list_barang.append((self.name, self.stock, self.value))

    def lihat_barang(self):
        print("Jumlah barang dagangan pada toko:", self.sum, "buah")
        for idx, barang in enumerate(self.list_barang, start=1):
            name, stock, value = barang
            print(f"{idx}. {name} seharga Rp {value} (stok: {stock})")

    def __del__(self):
        Dagangan.sum -= 1
        for barang in Dagangan.list_barang:
            if self.name in barang:
                Dagangan.list_barang.remove(barang)
                print(f"{self.name} dihapus dari toko!")
                break


# Contoh 
Dagangan1 = Dagangan("Galon Aqua 19L", 32, 17000)
Dagangan2 = Dagangan("Gas LPG 5 kg", 22, 88000)
Dagangan3 = Dagangan("Beras Ramos 5 kg", 13, 68000)
Dagangan1.lihat_barang()

print("\n")

del Dagangan1
Dagangan2.lihat_barang()
