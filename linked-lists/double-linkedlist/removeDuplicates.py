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

    def delete_node(self, node):
        current = self.head
        while current:
            #if it has only one item
            if current == node and current == self.head:
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
            elif current == node:
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

    def removeDuplicates(self):
        current = self.head
        seen = {} #hash table
        while current:
            if current.data not in seen:
                seen[current.data] = 1
                current=current.next
            else:
                nxt = current.next #currenti silinecek, current.nexte devam etmesi icin
                self.delete_node(current)
                current = nxt
        #print(seen)


    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

newlist = doubleLinkedList()
newlist.append(1)
newlist.append(4)
newlist.append(4)
newlist.append(6)
newlist.append(7)
newlist.append(7)
newlist.append(9)
newlist.removeDuplicates()

newlist.print_list()

