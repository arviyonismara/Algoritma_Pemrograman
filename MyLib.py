# Program MyLib
import random

def tambah(a,b):
    # keterangan dijawab oleh mahasiswa
    return a+b

def kurang(a,b):
    # keterangan dijawab oleh mahasiswa
    return a-b

def kali(a,b):
    # keterangan dijawab oleh mahasiswa
    return a*b

def bagiInt(a,b):
    # keterangan dijawab oleh mahasiswa
    return a//b

def bagiFloat(a,b):
    # keterangan dijawab oleh mahasiswa
    return a/b

def isiListRandom(A,n):
    # keterangan dijawab oleh mahasiswa
    for i in range(n):
        A[i] = random.randint(0,100)
        

def cetakList(A,n):
    # keterangan dijawab oleh mahasiswa
    for i in range(n):
        print(A[i],end=" ")
    print()

def lengthList(A):
    # keterangan dijawab oleh mahasiswa    
    i = 0
    for _ in A:
        i=i+1 # atau i+=1
    return i

def sumList(A,n):
    # keterangan dijawab oleh mahasiswa
    sum = 0
    for i in range(n):
        sum = sum+A[i]
    return sum

def AverageList (A,n):
    # keterangan dijawab oleh mahasiswa
    return sumList(A,n)/n

def MaxList(A,n):
    # keterangan dijawab oleh mahasiswa 
    max = A[0]
    for i in range(1,n):
        if A[i] > max:
            max = A[i]
    return max

def MinList (A,n):
    # keterangan dijawab oleh mahasiswa
    min = A[0]
    for i in range(1,n):
        if A[i] < min:
            min = A[i]
    return min
