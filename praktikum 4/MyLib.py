#praktikum 4 untuk kasus 3,4,5,6

#Ascending = mengurutkan dari kecil ke besar
#descending= mengurutkan dari besar ke kecil

#kasus 3
def BubbleSortA(n,A): #Ascending
    # n merupakan panjang array, A merupakan array
    # Kamus Lokal
    swap = False # kenapa false? karena agar dapat dijalankan di while
    # Algoritma
    while not swap: #pertukaran akan terjadi ketika dilakukan swap 
        swap = True
        for j in range(1, n): #misal jumlah n = 5 maka loop luarnya adalah 4
            if A[j-1]>A[j]: #disini ada sebuah pertukaran , jika lebih besar maka akan mengurutkan
                swap = False #loop akan terus dilakukan saat swap false (terjadi pertukaran)
                temp = A[j]
                A[j] = A[j-1]
                A[j-1] = temp
    return A

#kasus 4
def BubbleSortD(n,A): #Descending
    # n merupakan panjang array, A merupakan array
    # Kamus Lokal
    swap = False # kenapa false? karena agar dapat dijalankan di while
    # Algoritma
    while not swap: #pertukaran akan terjadi ketika dilakukan swap 
        swap = True
        for j in range(1, n): #misal jumlah n = 5 maka loop luarnya adalah 4
            if A[j-1]<A[j]: #disini ada sebuah pertukaran , jika lebih kecil maka akan mengurutkan
                swap = False #loop akan terus dilakukan saat swap false (terjadi pertukaran)
                temp = A[j]
                A[j] = A[j-1]
                A[j-1] = temp
    return A

def SelectionSortA(n,A):#Ascending
    i = 0    
    # Algoritma
    while i < n:
        min_idx = i #menyimpan index min
        for j in range (i+1, len(A)): #mencari index dan nilai min dari bagian yang belum urut 
            if A[min_idx] > A[j] : #pengecekan apakah lebih kecil 
                min_idx = j
        A[i], A[min_idx]=A[min_idx], A[i]
        i+=1
    return A

def SelectionSortD(n,A):
    i = 0    
    # Algoritma
    while i < n:
        max_idx = i #menyimpan index max
        for j in range (i+1, len(A)): #mencari index dan nilai max dari bagian yang belum urut 
            if A[max_idx] < A[j] : #pengecekan apakah lebih besar
                max_idx = j
        A[i], A[max_idx]=A[max_idx], A[i]
        i+=1
    return A

#kasus 5
def input3bil(A):
    A.append(int(input("masukan bilangan 1:")))
    A.append(int(input("masukan bilangan 2:")))
    A.append(int(input("masukan bilangan 3:")))
    A=BubbleSortA(len(A),A)
    return A

#kasus 6
def urutB(n,B):
    i1 = B[0]
    iN = B[len(B)-1]
    if i1 < iN :
        B=SelectionSortA(n,B)
    else:
        B=SelectionSortD(n,B)
    return B
    
        
