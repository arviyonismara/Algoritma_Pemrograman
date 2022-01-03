import MyLib

def main():
    A=[5, 2, 10, 27, 33]
    l=len(A)
    print(MyLib.InsertionSortA(l,A))
    print(MyLib.InsertionSortD(l,A))
    A= MyLib.input3bil(A)
    print(A)

#pemanggilan entry point
if __name__ == '__main__' :
    main()