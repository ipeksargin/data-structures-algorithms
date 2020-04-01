class Node:

    def __init__(self,key,leftChild,rightChild):
        self.key = key
        self.leftChild = None
        self.rightChild = None

    def insert(self,key):
        if self is None:
            self.key = Node(key)
            return
        
        if key < self.key:
            if self.leftChild:
                self.leftChild.insert(key)
            else:
                self.leftChild = Node(key)
                return 
        else:
            if self.rightChild:
                self.rightChild.insert(key)
            else:
                self.rightChild = Node(key)
                return
        
        

class binarySearchTree:
    def __init__(self,key):
        self.root = Node(key)

    def insert(self,key):
        self.root.insert(key)

def inorder(root):
    if root:
        inorder(root.leftChild)
        print(root.key)
        inorder(root.rightChild)

bst = binarySearchTree(6) #set the root value

bst.insert(1)
bst.insert(8)
bst.insert(9)
bst.insert(3)
inorder(bst.root)