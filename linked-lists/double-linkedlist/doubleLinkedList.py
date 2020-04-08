class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class doubleLinkedList:
    def __init__(self):
        self.head == None

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node

    def prepend(self,new_data): #add to front
        pass

    def print_list(self):
        pass
