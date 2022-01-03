from MyList import *

def main():
    objList = SLinkedList() #membuat headval
    objList.append("why") #fugnsi append pertama otomatis menjadi node1/head
    objList.append("I") #append ke node ke 2
    objList.append("love") #append node ke 3
    objList.append("programming!") #append node ke 4
    print('panjang:',objList.lengthlist()) #dicetak

if __name__ == "__main__":
    main()