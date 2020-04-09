class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class doubleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_data):
        if self.head == None:
            new_data = Node(new_data)
            self.head = new_data
            self.head.prev = None
        else:
            new_data = Node(new_data)
            current = self.head
            while current.next:
                current = current.next
            current.next = new_data
            current.next.prev = current
            new_data.next = None

    def prepend(self,new_data): #add to front
        if self.head == None:
            new_data = Node(new_data)
            self.head = new_data
            self.head.prev = None
        else:
            current = self.head
            new_data = Node(new_data)
            current.prev = new_data
            new_data.next = self.head
            self.head = new_data
            new_data.prev = None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def addAfter(self, new_data,key):
        current = self.head
        while current:
            if current.next is None and current.data == key: #if there is only one node
                new_data = Node(new_data)
                self.append(new_data)
                break
            elif current.data ==key:
                new_data = Node(new_data)
                nxt = current.next
                current.next = new_data
                new_data.next = nxt
                new_data.prev = current
                nxt.prev = new_data
            current = current.next

    def addBefore(self,new_data,key):
        current = self.head
        while current:
            if current.prev is None and current.data == key: #if there is only one node
                new_data = Node(new_data)
                self.append(new_data)
                break
            elif current.data == key:
                new_data = Node(new_data)
                prev = current.prev
                prev.next = new_data
                new_data.next = current
                current.prev = new_data
                new_data.prev = prev
            current = current.next

    def deleteNode(self, item):
        current = self.head
        while current:
            #if it has only one item
            if current.data == item and current == self.head:
                if current.next is None:
                    current = None
                    self.head = None
                    return

            #delete the head Node
                else:
                    nxt = current.next
                    nxt.prev = None
                    current.next = None
                    current = None
                    self.head = nxt
                    return
            #delete a node which isn't the last one
            elif current.data == item:
                if current.next is not None:
                    prev = current.prev
                    nxt = current.next
                    prev.next = nxt
                    nxt.prev = prev
                    current.next = None
                    current.prev = None
                    current = None
                    return
                else:
                    prev = current.prev
                    prev.next = None
                    cur.prev = None
                    current = None
                    return
            current = current.next

    def reverse(self):
        temp = None
        current = self.head
        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        if temp:
            self.head = temp.prev



double = doubleLinkedList()
double.append("A")
double.append("D")
double.prepend("B")
double.append("C")
double.append("X")
double.addAfter(11,"C")
double.addBefore(12,"C")
double.deleteNode("B")
double.reverse()
double.print_list()
