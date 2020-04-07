"""divide a circular linked list into two"""

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

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count +=1
            current = current.next
            if current == self.head:
                break
        return count

    def splitList(self):
        """A -> B -> C -> D should be A->B C-D"""
        size = len(self)

        if size == 0:
            return 0
        if size == 1:
            return self.head

        middle = size // 2
        count = 0

        current = self.head
        prev = None
        while current and count < middle:
            count +=1
            prev = current
            current = current.next
        #print(prev.data) #B
        #print(current.data) #C
        prev.next = self.head

        split_clist = CircularLinkedList() #to create a new blank linked list. geri kalani icin
        while current.next != self.head: #current is C
            split_clist.append(current.data)
            current = current.next
        split_clist.append(current.data) #appends the last item 

        self.printList()
        print("\n")
        split_clist.printList()

mylist = CircularLinkedList()
mylist.append("A")
mylist.append("B")
mylist.append("C")
mylist.append("D")
mylist.append("E")
mylist.append("F")

mylist.splitList()

