#kasus 2 dengan menggunakan caranya pak Moses

def main3 (a,b,c):
    return main2(main2(a,b),c)
def main2 (a,b):
    if a <= b :
        return a
    else:
        return b

a = int(input("masukan bilangan A : "))
b = int(input("masukan bilangan B : "))
c = int(input("masukan bilangan C : "))
main = main3(a,b,c)
print("bilangan terkecil adalah", main)