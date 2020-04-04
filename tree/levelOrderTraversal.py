import collections

class Tree:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

def levelOrderT(tree):
    if not tree:
        return 0
    else:
        nodes = collections.deque([tree])

        currentCount = 1
        nextCount = 0

    while (len(nodes) > 0):
        currentNode = nodes.popleft()
        currentCount -=1

        print(currentNode.data),

        if currentNode.left is not None:
            nodes.append(currentNode.left)
            nextCount +=1
        else:
            nodes.append("None")

        if currentNode.right is not None:
            nodes.append(currentNode.right)
            nextCount +=1
        
        if currentCount == 0:
            print ('\n')
            currentCount, nextCount = nextCount, currentCount

root = Tree(6)
root.left = Tree(9)
root.right = Tree(1)
root.left.left = Tree(5)
root.right.left = Tree(8)
root.right.right = Tree(12)

print(levelOrderT(root))

        




