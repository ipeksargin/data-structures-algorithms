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

    def isCircular(self, input_list):
        current = input_list.head
        while current.next:
            current = current.next
            if current.next == input_list.head:
                return "This is a circular linked list"
            return "This is not a circular linked list"

