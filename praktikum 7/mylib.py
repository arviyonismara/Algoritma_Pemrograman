def BinarySearch(A,cari):
    found = False
    batasbawah = 0 
    batasatas = len(A)-1 
    while batasbawah<=batasatas and not found:
        mid = (batasatas+batasbawah)//2 
        if A[mid] == cari:
            found = True
        else:
            if A[mid] > cari:
                batasatas = mid-1
            else:
                batasbawah = mid+1
    return found

def InsertionSortA(n,A):
    # n merupakan panjang array, A merupakan array
    # Kamus Lokal
    temp = 0    
    # Algoritma
    for i in range(1,n):
        temp = A[i]
        j = i-1
        while j>=0 and temp < A[j]:
            A[j+1] = A[j]
            j = j-1
        A[j+1]=temp
    return A