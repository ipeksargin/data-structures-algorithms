class BinaryTree:

    def __init__(self, root):
        self.root = root
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newValue):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newValue)
        else:
            new = BinaryTree(newValue)
            new.leftChild = self.leftChild
            self.leftChild = new

    def insertRight(self,newValue):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newValue)
        else:
            new = BinaryTree(newValue)
            new.rightChild = self.rightChild
            self.rightChild = new

    def getLeftChild(self):
        return self.leftChild
    
    def getRightChild(self):
        return self.rightChild

    def setRoot(self,newobj):
        self.root = newobj

    def getRoot(self):
        return self.root
    


first = BinaryTree("a")
print(first.getRoot())

first.insertLeft("b")
print(first.getLeftChild().getRoot()) ###to get the value

first.insertRight("c")
print(first.getRightChild().getRoot())
