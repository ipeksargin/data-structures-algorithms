#first in last out principle

class stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        if len(self.items) == 0:
            print("Stack is empty")
        
    def push(self,item):
        self.items.append(item)
        print(self.items)

    def pop(self):
        self.items.pop()
        print(self.items)

    def lastAdded(self):
        x = self.items[len(self.items)-1]
        print(x)


mys = stack()

mys.push(1)
mys.push("iki")
mys.push("three")
mys.lastAdded()
mys.pop()
    
