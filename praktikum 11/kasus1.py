def GetGenapList(L):
    n = len(L)
    newL = []
    for i in range(n):
        if L[i]%2==0:
            newL.append(L[i])
        return newL
def main():
    L=list(map(int,input().split(" ")))
    print(GetGenapList(L))

if __name__ == "__main__":
    main()
