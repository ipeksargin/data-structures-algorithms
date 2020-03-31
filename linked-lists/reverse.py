class Node():
    def __init__(self,next):
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def insertLast(self,new_data):
        if self.head is None:
            self.head = new_data
        else:
            lastNode = self.head
            while lastNode.next is not None: #lastnode nexti empty olana kadar
                if lastNode.next is None:
                    break
                else:
                    lastNode = lastNode.next
            lastNode.next = new_data #lastnode nexti empty ise, yeni node u lastnode next olarak ekle

    def reverse(self):
        current = self.head
        prev = None
        while current:
            nextn = current.next
            current.next = prev
            prev = current
            current = nextn
        self.head=prev
        print(current)

    def PrintList(self):

        if self.head is None:
            print("List is empty")
        return
        currentNode = self.head
        while currentNode is not None:
            print("x")
            print(currentNode.data)
            currentNode = currentNode.next



mylist = LinkedList()
a = Node("A")
b = Node("B")
c = Node("C")

mylist.insertLast(a)
mylist.insertLast(b)
mylist.insertLast(c)
mylist.reverse()
mylist.PrintList()
