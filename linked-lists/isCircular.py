"""we added LinkedList class to understand the difference between circular and single"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertLast(self,new_data):
        new_data = Node(new_data)

        if self.head == None:
            self.head == new_data
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_data
        
    def PrintList(self):
        if self.head is None:
            print("List is empty")
            return 
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.next


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

    def isCircular(self, inputList):
        current = inputList.head
        while current:
            current = current.next
            if current.next == inputList.head:
                return "This is a circular linked list"
        return "This is not a circular linked list"

mycirculList = CircularLinkedList()
mycirculList.append(1)
mycirculList.append(2)
mycirculList.append(3)
mycirculList.append(4)

myList = LinkedList() 
myList.insertLast(1)
myList.insertLast(2)
myList.insertLast(3)
myList.insertLast(4)

print(mycirculList.isCircular(mycirculList))
print(mycirculList.isCircular(myList))
