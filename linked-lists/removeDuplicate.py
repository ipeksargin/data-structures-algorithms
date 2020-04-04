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

    def removeDuplicate(self):
        if self.head == None:
            return "Empyt List"
        else:
            current = self.head
            prev = None
            nodes = {}
            while current is not None:
                if current.data in nodes: #check if there is conflict
                    prev.next = current.next #to remove the duplicate item
                    current = None
                else:
                    nodes[current.data] = 1
                    prev = current
                current = prev.next

    def printList(self):
        if self.head == None:
            return "Empyt List"
        else:
            current = self.head
            while current is not None:
                print(current.data)
                current = current.next


mylist = LinkedList()
print("Before Removing")
mylist.append(1)
mylist.append(6)
mylist.append(4)
mylist.append(4)
mylist.append(6)
mylist.append(7)
mylist.append(7)
mylist.printList()

print("After Removing")
mylist.removeDuplicate()
mylist.printList()




