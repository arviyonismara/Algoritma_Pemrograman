def tambah (a,b):
    return a+b

def kurang (a,b):
    return a-b

def kali (a,b):
    return a*b

def bagi (a,b):
    return a/b

def menu():
    print("tekan 1 untuk tambah")
    print("tekan 2 untuk kurang")
    print("tekan 3 untuk kali")
    print("tekan 4 untuk bagi")
    print("masukan pilihan anda :",end="")

while True :
    a = int(input("masukan bilangan A : "))
    b = int(input("masukan bilangan B : "))

    menu()
    x=input()
    if x == "1" :
        print(tambah(a,b))
    elif x == "2" :
        print(kurang(a,b))
    elif x == "3" :
        print(kali(a,b))
    elif x == "4" :
        print(bagi(a,b))
    else:
        print("opsi salah")
        
    print("ingin menghitung lagi? tekan y")
    x=input()
    if x != "y" :
        break


