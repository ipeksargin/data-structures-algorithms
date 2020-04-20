class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertEnd(self,new_item):
        if self.head == None:
            self.head = new_item
        else:
            current = self.head
            while current.next:
                current=current.next
            current.next=new_item

    def deleteEnd(self):
        current  = self.head
        while current.next is not None:
            previous = current
            current = current.next
        previous.next = None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
        
    def move_tail_to_head(self):
        previous = None #to keep the node before the last one. it will refer to null after removing the last
        last = self.head
        while last.next is not None:
            previous = last
            last = last.next
        last.next = self.head
        previous.next = None
        self.head = last
        
        


mylist = LinkedList()

first = Node(5)
mylist.insertEnd(first)

second = Node(6)
mylist.insertEnd(second)

third = Node(7)
mylist.insertEnd(third)

fourth = Node(8)
mylist.insertEnd(fourth)


#mylist.deleteEnd()
mylist.move_tail_to_head()
mylist.print_list()


