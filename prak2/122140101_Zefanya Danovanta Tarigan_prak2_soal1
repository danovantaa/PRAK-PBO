class Mahasiswa:
    def __init__(self, nama, NIM, angkatan, isMahasiswa = True ):
        self.nama = nama
        self.NIM = NIM
        self.angkatan = angkatan
        self.isMahasiswa = isMahasiswa

    def get_nama(self):
        return self.nama

    def set_nama(self, nama):
        self.nama = nama

    def get_NIM(self):
        return self.NIM

    def set_NIM(self, NIM):
        self.NIM = NIM

    def display_info(self):
        return f"Nama : {self.get_nama()} \nNIM : {self.get_NIM()} \nAngkatan : {self.angkatan} \n" \
               f"Status Mahasiswa : {'Aktif' if self.angkatan >=2017 and self.isMahasiswa else 'Non aktif'}"

    def Cek_Status(self):
        if self.angkatan <= 2017 or not self.isMahasiswa :
            return "Mahasiswa Sudah Tidak berkuliah lagi di ITERA "
        else : 
            return "Mahasiswa Aktif"

mahasiswa1 = Mahasiswa(nama="Zefanya Danovanta", NIM= "122140101", angkatan = 2022, isMahasiswa=True)
mahasiswa2 = Mahasiswa(nama="Nashrullah ", NIM="122140183", angkatan = 2022, isMahasiswa = False)
mahasiswa3 = Mahasiswa ( nama = "Arief", NIM = "122140083", angkatan = 2016, isMahasiswa = True )


print(mahasiswa1.display_info())
print(mahasiswa1.Cek_Status())

print("\n")

print(mahasiswa2.display_info())
print(mahasiswa2.Cek_Status())

print("\n")

print(mahasiswa3.display_info())
print(mahasiswa3.Cek_Status())
