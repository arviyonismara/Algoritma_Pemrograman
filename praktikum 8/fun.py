def fun(n, i = 2):   
    # Basis
    if (n <= 2): 
        return True if(n == 2) else False
    if (n % i == 0): 
        return False
    if (i * i > n): 
        return True 
    # Rekuren
    return fun(n, i + 1)

def main():
    n = 12
    if (fun(n)): #True
        print("merupakan bilangan fun")
    else:
        print("bukan merupakan bilangan fun")

if __name__ == "__main__":
    main()
