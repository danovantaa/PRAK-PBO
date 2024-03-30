class Hewan :
    def __init__(self, nama, JK):
        self.nama = nama
        self.JK = JK
    
    def bersuara (self):
        pass
    
    def makan(self):
        pass
    
    def minum (self):
        print(f'{self.nama} Sedang Minum Air')

class Kucing (Hewan):
    def __init__ (self, nama, JK):
        super().__init__(nama, JK)

    def bersuara(self):
        print(f'{self.nama} {self.nama} Bersuara : Meong !')

    def makan(self):
        print(f'{self.nama} Sedang makan Ikan')

class Anjing (Hewan): 
    def __init__ (self, nama, JK):
        super().__init__(nama, JK)

    def bersuara(self):
        print(f'{self.nama} {self.nama} Bersuara : GukGuk !')
    
    def makan(self):
        print(f'{self.nama} Sedang makan Tulang')


hewan1 = Kucing('Kiki' , 'Betina')
hewan2 = Anjing('Inchi' , 'Jantan')

print(hewan1.nama)
print(hewan2.nama)

hewan1.bersuara()
hewan1.makan()
hewan1.minum()

hewan2.bersuara()
hewan2.makan()
hewan2.minum()
