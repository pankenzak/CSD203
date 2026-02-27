class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def isEmpty(self):
        return self.root is None
    
    def insert(self, newValue):
        self.root = self._insert(self.root, newValue)

    def _insert(self, current, newValue):
        if current is None:
            newNode = Node(newValue)
            return newNode
        if newValue < current.data:
            current.left = self._insert(current.left, newValue)
        else:
            current.right = self._insert(current.right, newValue)

        return current

    def inOrder(self, current):
        if current is None:
            return
        self.inOrder(current.left)
        print(current.data, end = ' ')
        self.inOrder(current.right)

    def Search(self, current, value):
        if current is None:
            print(f'Not exist {value}')
            return False
        
        if value < current.data:
            return self.Search(current.left, value)
        elif value > current.data:
            return self.Search(current.right, value)
        else:
            print(f'Exist {value}')
            return True

    def findMin(self, current):
        while current.left != None:
            current = current.left
        return current

    def findMax(self, current):
        while current.right != None:
            current = current.right
        return current

    def Delete(self, current, value):
        if current is None:
            return
        if value < current.data:
            current.left = self.Delete(current.left, value)
        elif value > current.data:
            current.right = self.Delete(current.right, value)
        else:
            if current.left is None and current.right is None:
                return None 
            elif current.left is None:
                return current.right
            elif current.right is None:
                return current.left
            else:
                min_right = self.findMin(current.right)
                current.data = min_right.data
                current.right = self.Delete(current.right, min_right.data)
        return current
            
def main():
    bst = BinarySearchTree()
    bst.insert(20)
    bst.insert(10)
    bst.insert(25)
    bst.insert(30)
    bst.insert(5)
    bst.insert(15)
    bst.inOrder(bst.root)
    print()
    bst.Search(bst.root, 24)
    print()
    bst.root = bst.Delete(bst.root, 20)
    bst.inOrder(bst.root)

main()