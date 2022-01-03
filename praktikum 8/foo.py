def foo(n,A,key):
    if(n<0): #Basis 1
        return -1 #false / tidak ketemu
    if(A[n-1]==key): #Basis 2
        return 1 #True / ketemu
    else:
        return foo(n-1, A, key)

def main():
    Arr = [12,3,12,3,4]
    print(foo(len(Arr),Arr,))

if __name__ == "__main__":
    main()

