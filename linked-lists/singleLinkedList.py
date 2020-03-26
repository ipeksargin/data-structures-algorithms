
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def ListLength(self):
        currentNode = self.head
        length=0
        while currentNode is not None:
            length +=1
            currentNode = currentNode.next
        return length

    def insertHead(self,new_data):
        temporaryNode = self.head 
        self.head = new_data 
        new_data.next = temporaryNode 
        del temporaryNode

    def insertLast(self,new_data):
        if self.head is None:
            self.head = new_data
        else:
            lastNode = self.head
            while lastNode.next is not None: #lastnode nexti empty olana kadar
                if lastNode.next is None:
                    break
                else:
                    #John->Ben->Matthias
                    lastNode = lastNode.next
            lastNode.next = new_data #lastnode nexti empty ise, yeni node u lastnode next olarak ekle

    def insertAt(self, new_data, position):
        if position < 0 or position > self.ListLength():
            print("Invalid position")
        return 
        currentNode = self.head
        currentPosition = 0
        while currentPosition != position:
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition +=1
        previousNode.next = new_data
        new_data.next = currentNode

    def deleteEnd(self):
        currentNode = self.head
        while currentNode.next is not None:
            previous = currentNode
            currentNode = currentNode.next
        previous.next = None #en sondakini none reference et       
    
    def deleteAt(self,position):
        if position < 0 or position >= self.ListLength():
            print("Invalid position")
        return 
        currentNode = self.head
        currentPosition = 0
        while currentPosition != position:
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition +=1
        previousNode.next = currentNode.next

    def deleteHead(self):
        if self.head is not None:
            temporaryNode = self.head
            self.head = self.head.next
            temporaryNode.next = None
        else:
            print("This list is empty.")

    def PrintList(self):
        if self.head is None:
            print("List is empty")
            return 
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.next

linkedlist = LinkedList()


firstNode = Node("John")
linkedlist.insertLast(firstNode)

secondNode = Node("Ben")
linkedlist.insertLast(secondNode)

thirdNode = Node("Matthias")
linkedlist.insertLast(thirdNode)

fourthNode = Node("Jack")
linkedlist.insertHead(fourthNode)

fifthNode = Node("10")
linkedlist.insertAt(fifthNode, 3)
#linkedlist.insertAt(fifthNode, 10) returns invalid

linkedlist.deleteEnd()
linkedlist.deleteAt(1)
linkedlist.deleteHead()
#linkedlist.PrintList()


