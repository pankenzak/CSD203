class Node():
    def __init__(self, value):
        self.data = value
        self.next = None
        
class CicurlarLinkedList():
    def __init__(self):
        self.head = None
        
    def traversal(self):
        current = self.head
        if current == None:
            return print("None")
        while current.next != self.head:
            print(current.data, end = " -> ")
            current = current.next
            if current == self.head:
                return print(self.head.data)
            
    def insertAtBeginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = self.head
        
def main():
    cll = CicurlarLinkedList()
    seven = Node(7)
    cll.head = seven
    ten = Node(10)
    cll.head.next = ten
    ten.next = cll.head
    cll.traversal()
    two = Node(2)
    ten.next = two
    two.next = cll.head
    cll.traversal()
    cll.insertAtBeginning(6)
    cll.traversal()
    
main()