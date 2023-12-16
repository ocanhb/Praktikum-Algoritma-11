class Mahasiswa:
    mhscount = 0
    
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai
        Mahasiswa.mhscount += 1

    def displaycount(self): 
        print("Total Mahasiswa %d" % Mahasiswa.mhscount)
        
    def displaymahasiswa(self):
        print("Nama: ", self.nama) 
        print("Nilai: ", self.nilai)


def main():
    objek = Mahasiswa("", "")

    while True:
        print("\nProgram OOP\n1. Mendeklarasikan Objek\n2. Menampilkan Objek\n3. Merubah nilai objek\n4. Menghapus nilai objek\n5. Keluar dari program")
        pilihan = input("\nmasukkan pilihan berupa angka (1/2/3/4/5) : ")

        if pilihan == "1":
            nama = input("masukkan namamu : ")
            nilai = input("masukkan nilaimu : ")
            objek = Mahasiswa(nama, nilai)
            print("\ndata berhasil ditambahkan")

        elif pilihan == "2":
            objek.displaymahasiswa()

        elif pilihan == "3":
            field = input("apa yang ingin dirubah (nama/nilai) : ")
            value = input(f"masukkan {field} : ")
            if field.lower() == "nama":
                objek.nama = value
                print("\ndata nama berhasil dirubah")
            elif field.lower() == "nilai":
                objek.nilai = value
                print("\ndata nilai berhasil dirubah")
            else:
                print("\nfield tidak valid")

        elif pilihan == "4":
            objek = Mahasiswa("", "")
            print("\ndata berhasil dihapus")

        elif pilihan == "5":
            print("terimakasih telah menggunakan program ini")
            break

        else:
            print("\npilihan tidak valid. Silakan masukkan angka 1-5.")


if __name__ == "__main__":
    main()
