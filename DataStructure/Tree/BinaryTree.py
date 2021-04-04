
class BinTree:

    class BinTreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self, data):
        self.root : BinTree.BinTreeNode = BinTree.BinTreeNode(data)
    
    def insertLeft(self, parent : BinTreeNode , data):

        if parent != None:
            if parent.left == None:
                parent.left = BinTree.BinTreeNode(data)
            else:
                raise IndexError(f'parent - {parent.data} [insertLeft] - Already exist Node')
        else:
            raise IndexError(f'Not Exist Parent Node')
        
        return parent.left

    def insertRight(self, parent : BinTreeNode, data):

        if parent != None:
            if parent.right == None:
                parent.right = BinTree.BinTreeNode(data)
            else:
                raise IndexError(f'parent - {parent.data} [insertRight] - Already exist Node')
        else:
            raise IndexError(f'Not Exist Parent Node')
        
        return parent.right
    
    def getRoot(self):
        return self.root
    
    def getLeft(self, parent : BinTreeNode):
        if parent != None:
            return parent.left
        else:
            raise IndexError(f'Not Exist Parent Node')
    
    def getRight(self, parent : BinTreeNode):
        if parent != None:
            return parent.right
        else:
            raise IndexError(f'Not Exist Parent Node')

    def display(self, parent : BinTreeNode):
        if parent != None:
            self.display(parent.left)
            print(parent.data ,end=' >>> ')
            self.display(parent.right)
            


mybinTree = BinTree(1)

mybinTree.insertLeft(mybinTree.getRoot(), 2)
mybinTree.insertRight(mybinTree.getRoot(), 3)

# mybinTree.getLeft(mybinTree.getRoot()).insertLeft(mybinTree.getLeft(), 4)
# mybinTree.getLeft(mybinTree.getRoot()).insertRight(mybinTree.getLeft(), 5)

# mybinTree.getRight().insertLeft(mybinTree.getRight(), 6)
# mybinTree.getRight().insertRight(mybinTree.getRight(),7)

mybinTree.display(mybinTree.getRoot())