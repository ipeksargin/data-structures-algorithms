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

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count +=1
            current = current.next
            if current == self.head:
                break
        return count


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

    def removeNodes(self,node): #remove nodes instead of keys.
        if self.head == node: #if it is the head you want to remove
            current = self.head
            while current.next != self.head: #en sondaki node head'e bagli oldugu icin ulasmasi lazim
                current = current.next
            current.next = self.head.next #point last node to the next after head
            self.head = self.head.next #point to next after head
        else:
            current = self.head
            prev = None
            while current.next != self.head:
                prev = current
                current = current.next
                if current == node:
                    prev.next = current.next
                    current = current.next #

    def josephusCircle(self, step):
        if len(self) == 0: return 0
        current = self.head

        while len(self) > 1:
            count =1
            while count != step:
                current = current.next
                count +=1
            print("Removed: " + str(current.data))
            self.removeNodes(current)
            current = current.next



mylist = CircularLinkedList()
mylist.append(1)
mylist.append(2)
mylist.append(3)
mylist.append(4)
mylist.josephusCircle(2)


mylist.printList()


