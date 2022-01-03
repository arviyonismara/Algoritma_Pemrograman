import MyLib
#praktikum 4 untuk kasus 3,4,5,6
#entry point dengan prosedur main
def main() :
    Arr=[1,5,8,2,5,7,9,10]
    B =[15, 12, 20, 50, 100]
    l=len(Arr)
    #kasus 3
    print(MyLib.BubbleSortA(l,Arr))
    print(MyLib.BubbleSortD(l,Arr))
    #kasus 4
    print(MyLib.SelectionSortA(l,Arr))
    print(MyLib.SelectionSortD(l,Arr))
    #kasus 5
    Arr= MyLib.input3bil(Arr)
    print(Arr)
    #kasus 6
    print(MyLib.urutB(len(B),B))
    print('masukan bilangan untuk indeks ke 0: ',end="")
    B.insert(0,int(input()))
    print(MyLib.urutB(len(B),B))

#pemanggilan entry point
if __name__ == '__main__' :
    main()


