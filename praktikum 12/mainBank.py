from AkunBank import*
def main():
    # Buat objek akun bank anda dengan nama terserah
    # Lakukan instance kepada class AkunBank
    # contoh: myakun = AkunBank("Lala",12312,1000)
    # parameter pertama di isi nama "Adi"
    # parameter kedua di isi no rek 1234567
    # parameter ketiga di isi saldo sebesar 100000
    # MULAI (1 baris)
    akunku = AkunBank('Boy',133246)
    # SELESAI
    akunku.LihatSaldo()
    # Panggil method Menabung dengan diisi uang sebesar 20000
    # # MULAI (1 baris)
    # # SELESAI
    akunku.LihatSaldo()
    akunku.Mengambil(100000)
    akunku.LihatSaldo()

if __name__ == "__main__":
    main()
