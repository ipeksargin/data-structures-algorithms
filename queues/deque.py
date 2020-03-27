"""Deque is a different data structure than stacks and queues.
You can do insertion and deletion from both front and back."""

class deque():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        if len(self.items) == 0:
            print("This is empty.")

    def addFront(self,item):
        self.items.append(item) #stack implementation
        print(self.items)

    def addBack(self,item):
        self.items.insert(0,item) #queue implementation
        print(self.items)

    def removeFront(self):
        self.items.pop()
        print(self.items)

    def removeBack(self):
        self.items.pop(0)
        print(self.items)

    def size(self):
        length = len(self.items)
        print(length)
    
myDeque = deque()

myDeque.addFront("one")
myDeque.addFront("two")
myDeque.addFront("three")

myDeque.addBack(11)
myDeque.addBack(12)
myDeque.addBack(13)

