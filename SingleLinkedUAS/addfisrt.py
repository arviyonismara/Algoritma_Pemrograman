from MyList import *
def main():
    objList = SLinkedList()#membuat head
    n1 = Node("siang") #node 1
    objList.headval = n1 #mengarahkan pointer head ke n1
    n2 = Node("sore") #membuat node untuk 2
    n3 = Node("malam") #membuat node untuk 3
    objList.headval.nextval = n2 #membuat link ke n2
    n2.nextval = n3 #dilanjutkan ke n3
    objList.addfirst("pagi")  #fungsi dieksekusi
    objList.listprint() #di cetak

if __name__ == "__main__":
    main()