# Arvie Arvearie Yonismara
# A11.2020.12792
# A11.4214
class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval,end="-->")
            printval = printval.nextval

    def listprintbyIndex(self,index):
        printval = self.headval
        count = 0
        while printval is not None:
            if index == count:
                print (printval.dataval)
                break
            printval = printval.nextval
            count+=1
        if printval is None:
            print('indeks diluar batas')

    def append(self, newdata):
        NewNode = Node(newdata) #membuat objek NewNode
        if self.headval is None: #cek apakah lit kosong atau tidak
            self.headval = NewNode #jika kosong isi headval dengan NEwNode
            return
        lastelm = self.headval #jika ada isinya, buat variabel penampung untuk elemen terakhir
        while(lastelm.nextval is not None): #melakukan pengulangan dan assign lastelm dengan elemen berikutnya
            lastelm = lastelm.nextval
        lastelm.nextval=NewNode #assign nextval dari lastelm NewNode

    def addfirst(self,newdata):
        NewNode = Node(newdata) #membuat objek NewNode
        NewNode.nextval = self.headval #assign NewNode denga elemen pertama/head
        self.headval = NewNode #assign headval dengan NewNode

    def addmidle(self,middle_node,newdata):
        if middle_node is None: #mengetahui jika indeks tengah kosong atau tidak
            print("node tidak ada isi")
            return
        NewNode = Node(newdata) #membuat objek NewNode
        NewNode.nextval = middle_node.nextval #assign nextval dengan middle node
        middle_node.nextval = NewNode #assign middle node dengan NewNode
    
    def remove(self, Removekey):
        headval = self.headval #membuat objek self.headval
        if headval is not None: #jika head memiliki node yang akan dihapus
            if headval.dataval == Removekey: #mengetahui jika dataval sama dengan dataval kunci
                self.head = headval.nextval
                headval = None #dilakukan penghapusan dataval pada dataval yang sama dengan kunci
                return
        #mencari key untuk di remove, terus mencari dari node sebelumnya 
        while headval is not None:
            if headval.dataval == Removekey:
                break
            prev = headval
            headval = headval.nextval
        #jika key tidak ada di linked list
        if headval == None:
            return
        #unlink node dari link list
        prev.nextval = headval.nextval
        headval = None 

    def lengthlist(self):
        count = 0 #inisialisai count = 0
        temp = self.headval #assign variabel temp ke headval
        while temp:
            count+=1 #increment untuk menghitung jumlah
            temp = temp.nextval #akan terus me link sampai none
        return count

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

