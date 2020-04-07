"""Remove a key from circuled linked list"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_data):
        if self.head == None:
            self.head = Node(new_data)
            self.head.next = self.head
        else:
            newNode = Node(new_data)
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = newNode
            newNode.next = self.head

    def printList(self):
        if self.head == None:
            return "Empyt List"
        else:
            current = self.head
            while current:
                print(current.data)
                current = current.next
                if current == self.head:
                    break

    def remove(self,key):
        if self.head.data == key: #if it is the head you want to remove
            current = self.head
            while current.next != self.head: #en sondaki node head'e bagli oldugu icin ulasmasi lazim
                current = current.next
            current.next = self.head.next #point last node to the next after head
            self.head = self.head.next #point to next after head
        else:
            current = self.head
            prev = None
            while current.next != self.head:
                prev = current
                current = current.next
                if current.data == key:
                    prev.next = current.next
                    current = current.next #

mylist = CircularLinkedList()
mylist.append("A")
mylist.append("B")
mylist.append("C")
mylist.append("D")
mylist.append("E")
mylist.append("F")

mylist.remove("B")
mylist.remove("E")


mylist.printList()


