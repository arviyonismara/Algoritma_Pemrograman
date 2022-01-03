from MyList import *
def main():
    objList = SLinkedList()#membuat head
    n1 = Node("pagi") #buat node 1 n1
    objList.headval = n1 #mengarahkan pointer head ke n1
    n2 = Node("siang") #membuat node untuk n2
    n3 = Node("malam") #membuat node untuk n3
    n4 = Node("subuh") #membuat node untuk n4
    objList.headval.nextval = n2 #mengarahkan link node 2
    n2.nextval = n3 #dilanjutkan ke n3
    n3.nextval = n4 #dilanjutkan ke n4
    objList.remove('siang')
    objList.listprint()

if __name__ == "__main__":
    main()