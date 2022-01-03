#variabel global list
AId=[]
ABrg=[]
AHrg=[]

def InputData(arrId, arrBarang, arrHarga, n):
    for i in range(n):
        AId.append(arrId[i])
        ABrg.append(arrBarang[i])
        AHrg.append(arrHarga[i])
def LihatData(n):
    print('ID NAMA HARGA BARANG')
    for i in range (n):
        print(AId[i], ABrg[i], AHrg[i])
def LihatDataTerurut(n):
    tempid = 0
    tempNama = ''
    tempHarga = 0  
    # Algoritma
    for i in range(1,n):
        tempid = AId[i]
        tempNama = ABrg[i]
        tempHarga = AHrg[i]
        j = i-1
        while j>=0 and tempid < AId[j]:
            AId[j+1] = AId[j]
            ABrg[j+1] = ABrg[j]
            AHrg[j+1] = AHrg[j]
            j = j-1
        AId[j+1]=tempid
        ABrg[j+1]=tempNama
        AHrg[j+1]=tempHarga
    print('ID NAMA HARGA BARANG')
    for i in range (n):
        print(AId[i], ABrg[i], AHrg[i])