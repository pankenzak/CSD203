class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self, current):
        if current == None:
            return
        print(current.data, end = " ")
        self.pre_order(current.left)
        self.pre_order(current.right)

    def in_order(self, current):
        if current == None:
            return
        self.in_order(current.left)
        print(current.data, end = ' ')
        self.in_order(current.right)

    def post_order(self, current):
        if current == None:
            return
        self.post_order(current.left)
        self.post_order(current.right)
        print(current.data, end = ' ')

def main():
    seven = Node(7)
    bt = BinaryTree()
    bt.root = seven
    four = Node(4)
    three = Node(3)
    six = Node(6)
    two = Node(2)
    five = Node(5)
    eight = Node(8)
    seven.left = four
    seven.right = two
    four.left = five
    four.right = six
    two.right = eight    
    bt.pre_order(bt.root)
    print()
    bt.in_order(bt.root)
    print()
    bt.post_order(bt.root)

main()