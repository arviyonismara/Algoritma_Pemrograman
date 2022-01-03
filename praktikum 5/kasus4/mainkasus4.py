# Program: Pendataan Barang
import MyLib
# Kamus
n=int(input('Masukkan kapasitas barang:')) # n bertipe integer
arrId= [int]*n #adalah array of integer dengan panjang n
arrBarang= [str]*n #adalah array of string dengan panjang n
arrHarga= [int]*n #adalah array of integer dengan panjang n
menu='1'
# Algoritma
while menu != '0' :
    print('Kapasitas Barang:',n)
    print('Pilih Menu (Ketik 1/2/3 dan 0 untuk keluar')
    print('1. Input Data')
    print('2. Lihat Data')
    print('3. Lihat Data Terurut')
    print('ketikan :',end='')
    menu = input()
    if menu == '1' :
        for i in range (n):
            print('Data ke-',i+1)
            arrId[i]=input('masukan Id: ')
            arrBarang[i]=input('masukan nama barang: ')
            arrHarga[i]=input('masukan harga: ')
        MyLib.InputData(arrId, arrBarang, arrHarga, n)
    elif menu == '2':
        MyLib.LihatData(n)
    elif menu == '3':
        MyLib.LihatDataTerurut(n)
    elif menu == '0':
        break

