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


    def rotate(self,k):
        if self.head and self.head.next is None:
            return "Empty list"
        else:
            prev = None
            p = self.head
            q = self.head
            count = 0
            while p and count < k:
                prev = p
                p = p.next
                q = q.next
                count = count + 1
            p = prev

            while q:
                prev = q
                q = q.next
            q = prev
            #print("q",q.data)

            q.next = self.head # en sondakini en basa bagla
            self.head = p.next
            p.next = None
        
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
mylist.append(1)
mylist.append(2)
mylist.append(3)
mylist.append(4)
mylist.append(5)
mylist.append(6)
mylist.append(7)
mylist.append(8)
mylist.printList(),
print("Rotated list: ")
mylist.rotate(3)
mylist.printList()

