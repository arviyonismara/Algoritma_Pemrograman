def BinarySearch(A,cari):
    idx=[]
    found = False
    batasbawah = 0 
    n=len(A)
    batasatas = n-1
    i=0
    while batasbawah <= batasatas and not found:
        mid = (batasatas+batasbawah)//2 
        if A[mid] == cari:
            found = True
            print(cari,'pada A',found,end=',')
        else:
            if A[mid] > cari:
                batasatas = mid-1
            else: # if A[mid] < cari:
                batasbawah = mid+1                
    for i in range(n):
        if A[i] == cari:
            found = True
            idx.append(i)
    if found == True:
        print('jumlahnya',len(idx),end=' ')
        print('pada indeks ', end=' ')
        for i in range (len(idx)):
            print(idx[i], end=' ')
    else:
        print('tidak terdapat',cari,'pada A')

