class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def length(self):
        current = self.head
        length = 0
        while current is not None:
            length +=1
            current = current.next
        return length

    def insertEnd(self,new_item):
        if self.head is None:
            self.head = new_item
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_item

    def findNode(self,n):
        current = self.head
        num = 1
        while current is not None:
            current = current.next
            num = num + 1
            if num == n:
                print("Node is",current.data)


    def printList(self):
        current = self.head
        while current:
            print(current.data),
            current = current.next



mylist = LinkedList()

first = Node("one")
mylist.insertEnd(first)

second = Node("two")
mylist.insertEnd(second)

third = Node("three")
mylist.insertEnd(third)

last = Node("four")
mylist.insertEnd(last)

five = Node("five")
mylist.insertEnd(five)

six = Node("six")
mylist.insertEnd(six)


mylist.findNode(5)
mylist.printList()
