import mylib

def main():
    A = [1,5,8,9,20,20,20,20,50]
    print('A =',A)
    c=int(input('masukan bilangan yang dicari : '))
    mylib.BinarySearch(A,c)

if __name__ == '__main__' :
    main()