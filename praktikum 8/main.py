import pustaka

def main():
    a =int(input('masukkan bilangan a: '))
    b =int(input('masukkan bilangan b: '))
    print('a+b=',pustaka.jumlah(a,b))
    print('a-b=',pustaka.kurang(a,b))
    print('a*b=',pustaka.kali(a,b))
    print('a^b=',pustaka.pow(a,b))
    print('a!=',pustaka.fact(a))
    print('b!=',pustaka.fact(b))
    
 
if __name__ == '__main__':
    main()
