"""In circular linked list, the last node points to the head node instead of null."""

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


    def prepend(self, new_data): #front append
        current = self.head
        newNode = Node(new_data)
        if self.head == None:
            newNode.next = newNode
        else:
            newNode.next = self.head
            while current.next != self.head:
                current = current.next
            current.next = newNode
            self.head = newNode


mylist = CircularLinkedList()
mylist.append(1)
mylist.append(6)
mylist.append(4)
mylist.prepend(4)
mylist.append(6)
mylist.append(7)
mylist.append(7)
mylist.printList()
