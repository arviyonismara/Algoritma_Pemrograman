import MyLib

#kasus 1
def main():
    # A=[5, 2, 10, 27, 33,10]
    # A=[1,5,2,10,15]
    # A=[5,5,5,6,5,5,5]
    A=[5,2,10,27,33]
    print('A=',A)
    c = int(input("masukkan angka yang dicari: "))
    # ##kasus 1
    print(c,'pada A=',MyLib.SequentialSearch(A,c))
    ##kasus 2
    # print(c,'pada A, terdapat pada indeks',MyLib.SequentialSearchM(A,c))
    # MyLib.SequentialSearchM2(A,c)
    ##kasus 3
    #A = [12, 15, 20, 50, 100]
    # A = [27,5,2,10,33,500,7,49]
    # print('A=',A)
    # c = int(input('masukan bilangan k:'))
    # print(c,'pada A =',MyLib.linearsearchsentinel(c,len(A),A))

if __name__ == '__main__':
    main()
