#first in first out principle
class queue():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        if len(self.items)==0:
            print("This queue is empty.")
        else:
            print("not empty")

    def enqueue(self,item):
        self.items.insert(0,item) 
        print(self.items)

    def dequeue(self):
        self.items.pop()
        print(self.items)

myq = queue()
myq.enqueue("one")
myq.enqueue(2)
myq.enqueue(6)
myq.enqueue("ten")

myq.dequeue()


#myq.isEmpty()

