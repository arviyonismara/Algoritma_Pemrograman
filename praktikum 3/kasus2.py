#praktikum 3 kasus 2
#membandingkan bilangan dari kasus 1 dengan menambahkan bilangan C

def main2 (a,b,c):
    if a < b and a < c :
        print("bilangan terkecil adalah bilangan A yaitu", a)
    elif b < a and b < c:
        print("bilangan terkecil adalah bilangan B yaitu", b)
    else:
        print("bilangan terkecil adalah bilangan C yaitu", c)

a = int(input("masukan bilangan A : "))
b = int(input("masukan bilangan B : "))
c = int(input("masukan bilangan C : "))
main2(a,b,c)