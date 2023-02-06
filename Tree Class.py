
class Node(object):

    def __init__(self, left: int, data, right: int):
        """Takes node in the form (left, data right)"""
        self.__left = left
        self.__right = right
        self.__data = data

    def setRight(self, newRight: int) -> None:
        """Sets right pointer to point to a new location."""
        self.__right = newRight

    def setLeft(self, newLeft: int) -> None:
        self.__left = newLeft

    def setData(self, newData) -> None:
        self.__data = newData

    def getRight(self) -> int:
        return self.__right

    def getLeft(self) -> int:
        return self.__left
    
    def getData(self):
        return self.__data

    def __str__(self):
        """Returns node data as an array in the form [left, data, right]"""
        return ", ".join([str(self.__left), str(self.__data), str(self.__right)])
    

    
class BinaryTree(object):
    
    def __init__(self, rootData):
        self.__tree = [Node(-1, rootData, -1)]

    def addNode(self, data: int) -> None:
        """Adds a node at the correct place in the tree. If it is the same it goes left."""
        newNode = Node(-1, data, -1)
        self.__tree.append(newNode) #add node but its not connected to anything yet
        indexOfNewNode = len(self.__tree) - 1
        atEnd = False
        currentIndex = 0
        while not atEnd:
            print(currentIndex, len(self.__tree))
            currentNodeData = self.__tree[currentIndex].getData()
            if int(data) > int(currentNodeData):
                goRight = True
                nextIndex = self.__tree[currentIndex].getRight()
            else:
                goRight = False
                nextIndex = self.__tree[currentIndex].getLeft()
            if nextIndex == -1: #you can add to it, atEnd = True
                if goRight:
                    self.__tree[currentIndex].setRight(indexOfNewNode)
                else:
                    self.__tree[currentIndex].setLeft(indexOfNewNode)
                atEnd = True
            else:
                currentIndex = nextIndex

    def inOrder(self):
        values = []
        for node in self.__tree:
            values.append(node.getData())
        return sorted(values)

    def preOrder(self) -> list:
        """Return a list of nodes from the tree in pre-order"""
        
        def preOrderRecursionFunction(index, values):
            node = self.__tree[index]
            values.append(node.getData())
            if node.getLeft() != -1:
                values = preOrderRecursionFunction(node.getLeft(), values)
            if node.getRight() != -1:
                values = preOrderRecursionFunction(node.getRight(), values)
            return values
        
        values = preOrderRecursionFunction(0, [])
        return values

    def postOrder(self):
        pass

    def display(self):
        for node in self.__tree:
            print(node)

tree = BinaryTree(5)
tree.addNode(1)
#tree.display()
tree.addNode(3)
tree.addNode(2)
tree.addNode(7)
#tree.display()
tree.addNode(5)
tree.addNode(4)
#tree.display()
tree.addNode(6)
print(tree.preOrder())