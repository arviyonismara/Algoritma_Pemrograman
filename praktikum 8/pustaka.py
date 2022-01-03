def jumlah(a,b):
    'menjumlahkan a dan b secara rekursif'
    if b == 0 :
        return a
    else:
        return 1 + jumlah(a,b-1)
def kurang (a,b):
    'mengurangkan a dan b secara rekursif'
    if b == 0 :
        return a
    else:
        #return a - kurang(a,b-1)
        return kurang(a-1,b-1)
def kali(a,b):
    'mengkalikan a dan b secara rekursif'
    if b==1:
        return a
    else:
        return a + kali(a,b-1)
def pow(a,b):
    'memangkatkan a dan b secara rekursif'
    if b==1:
        return a
    else:
        return a * pow(a,b-1)
def fact(a):
    'menampilkan deret factorial dan hasilnya secara rekursif'
    if a == 1:
        return 1
    else: 
        return a * fact(a-1)