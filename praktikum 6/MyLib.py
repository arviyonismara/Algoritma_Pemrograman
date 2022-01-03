#praktikum 6

def SequentialSearch(A,cari):
    found = False
    n=len(A)
    i=0
    while i<n:
        i=i+1
        if A[i]==cari:
            found = True
            break
    # for i in range(n):
    #     if A[i] == cari:
    #         found = True
    return found

def SequentialSearchM(A,cari):
    found = False
    n=len(A)
    i=0
    for i in range(n):
        if A[i] == cari:
            found = True
            break
    if found == True:
        print(found)
        return i
    else:
        return -1

def SequentialSearchM2(A,cari):
    idx=[]
    found = False
    n=len(A)
    i=0
    for i in range(n):
        if A[i] == cari:
            found = True
            idx.append(i)
    if found == True:
        print(cari,'pada A terdapat pada indeks ', end=' ')
        for i in range (len(idx)):
            print(idx[i], end=' ')
        print(' countnya adalah',len(idx))
    else:
        print('tidak terdapat',cari,'pada A')
    
def linearsearchsentinel(k,n,a):
    
    found= False
    templast = a[n - 1] 
    a[n-1] = k
    i = 0
    while a[i] != k :
        i+=1
    a[n-1] = templast
    print('jumlah loop',i)
    if i < n-1 or k == a[n-1]:
        found = True

    return found
