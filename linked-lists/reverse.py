class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,new_data):
        new_data = Node(new_data)
        if self.head == None:
            self.head = new_data
            return
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_data

    def reverse(self):
        if self.head == None:
            return "Empyt list"
        else:
            prev = None
            current = self.head
            while current is not None: #until the end of the list
                nxt = current.next
                current.next = prev
                prev = current
                current = nxt
            self.head=prev

    def printList(self):
        if self.head == None:
            return "Empyt list"
        else:
            current = self.head
            while current is not None:
                print(current.data)
                current = current.next



mylist = LinkedList()
print("Normal list: ")
mylist.append("A")
mylist.append("B")
mylist.append("C")
mylist.append("D")
mylist.printList()
print("Reversed List:")
mylist.reverse()
mylist.printList()

