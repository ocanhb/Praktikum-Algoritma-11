class Mahasiswa:
    mhscount = 0
    
    def __init__(self, nama, nim, angkatan):
        self.nama = nama
        self.nim = nim
        self.angkatan = angkatan
        Mahasiswa.mhscount += 1

    def displaycount(self): 
        print("Total Mahasiswa %d" % Mahasiswa.mhscount)
        
    def displaymahasiswa(self):
        print("Nama: ", self.nama) 
        print("NIM: ", self.nim)
        print("angkatan", self.angkatan)
        
nama = input("Masukkan nama kamu: ")
nim = input("Masukkan NIM kamu: ")
angkatan = input ("masukkan angkatan kamu: ")

print("\n")
mhs1 = Mahasiswa(nama, nim, angkatan)
mhs1.displaymahasiswa()

print("\n")
mhs1.displaycount()
