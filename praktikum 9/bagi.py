def bagi (a,b):
    if a < b : #basis a<b 
        return 0
    else:#rekurens
        return 1+bagi(a-b,b) #contoh 1+(6-5,5)
                             #1+0=1
a=int(input('masukan angka a: '))
b=int(input('masukan angka b: '))
print('a/b=',bagi(a,b))