
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,new_data):
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
linkedlist.insert(firstNode)

secondNode = Node("Ben")
linkedlist.insert(secondNode)

thirdNode = Node("Matthias")
linkedlist.insert(thirdNode)

linkedlist.PrintList()


