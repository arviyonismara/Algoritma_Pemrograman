import mylib

def main():
    # kasus 1
    A = [2,5,10,27,33]
    print('A =',A)
    c=int(input('masukan bilangan yang dicari : '))
    print(c,'pada A= ',mylib.BinarySearch(A,c))

    # kasus2
    # A = [10,2,5,33,27]
    # print('A =',A)
    # c=int(input('masukan bilangan yang dicari : '))
    # print(c,'pada A= ',mylib.BinarySearch(mylib.InsertionSortA(len(A),A),c))

if __name__ == '__main__' :
    main()