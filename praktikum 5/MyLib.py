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

def InsertionSortD(n,A):
    # n merupakan panjang array, A merupakan array
    # Kamus Lokal
    temp = 0    
    # Algoritma
    for i in range(1,n):
        temp = A[i]
        j = i-1
        while j>=0 and temp > A[j]:
            A[j+1] = A[j]
            j = j-1
        A[j+1]=temp
    return A

def input3bil(A):
    A.append(int(input("masukan bilangan 1:")))
    A.append(int(input("masukan bilangan 2:")))
    A.append(int(input("masukan bilangan 3:")))
    A=InsertionSortA(len(A),A)
    return A