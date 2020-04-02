import sys
class Tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def checkBst(node, mini, maxi):
    # if it is empty
    if node == None:
        return 1

    if node.data < mini:
        return 0
    if node.data > maxi:
        return 0

    return checkBst(node.right,node.data,maxi) and checkBst(node.left,mini,node.data)

root = Tree(6) 
root.left = Tree(3) 
root.right = Tree(9) 
root.left.left = Tree(1) 
root.left.right = Tree(5) 
root.right.left = Tree(7)
root.right.right = Tree(11)
mini = -sys.maxsize -1
maxi = sys.maxsize

if(checkBst(root,mini, maxi)):
    print("This is a binary search tree")
else:
    print("This is not a binary search tree")
