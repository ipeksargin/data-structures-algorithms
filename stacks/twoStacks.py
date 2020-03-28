#two stacks behaving like a queue

class stack:
    def __init__(self):
        self. instack = []
        self.outstack = []


    def enqueue(self,element):
        self.instack.append(element) #append the item to instack
        print(self.instack)

    def dequeue(self):
        if not self.outstack: #empty list -> boolean false -> if true
            while self.instack:
                pops = self.instack.pop()
                self.outstack.append(pops)
                #print(pops)
                print(self.outstack)

        else:
            print("outstack is empty")


ins = stack()

ins.enqueue("one")
ins.enqueue("two")
ins.enqueue("three")
ins.enqueue("four")
ins.dequeue()


