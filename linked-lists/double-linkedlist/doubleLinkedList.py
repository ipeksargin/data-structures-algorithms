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

double = doubleLinkedList()
double.append("A")
double.append("D")
double.append("X")
double.append("C")
double.prepend("B")
double.print_list()