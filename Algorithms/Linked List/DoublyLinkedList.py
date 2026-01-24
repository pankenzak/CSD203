class Node:
    def __init__(self, value):
        self.data = value
        self.prev = None
        self.next = None
 
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def length(self):
        current = self.head
        length = 0
        if current == None:
            return length
        while current.next != None:
            current = current.next
            length += 1
        return length
    
    def traversal(self):
        current = self.head
        print("None", end = " <-> ")
        while current != None:
            print(current.data, end = " <-> ")
            current = current.next
        print("None")
        
    def backward_traversal(self):
        current = self.head
        print("None", end = " <-> ")
        if self.head == None:
            return print("None")
        while current.next != None:
            current = current.next
        while current != None:
            print(current.data, end = " <-> ")
            current = current.prev
        print("None")

    def insertAtBeginning(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        
    def insertAtEnd(self, value):
        new_node = Node(value)
        if self.head == None:
            self.insertAtBeginning(value)
            return
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node
        new_node.prev = current
        
    def insertAtPosition(self, value, position):
        pos = 0
        current = self.head
        new_node = Node(value)
        while pos < position - 1:
            current = current.next
            pos += 1
        new_node.next = current.next
        current.next = new_node
        new_node.prev = current
        
    def deleteAtBeginning(self):
        if self.head == None:
            return Node(None)
        tmp = self.head
        self.head = self.head.next
        self.head.prev = None
        return tmp
    
    def deleteAtEnd(self):
        current = self.head
        if current == None:
            return Node(None)
        while current.next.next != None:
            current = current.next
        tmp = current.next
        current.next = None
        return tmp
    
    def deleteAtPosition(self, position):
        if self.head == None:
            return Node(None)
        if position <= 0:
            return self.deleteAtBeginning()
        if position >= self.length():
            return self.deleteAtEnd()
        pos = 0
        current = self.head
        
        while pos < position - 1:
            current = current.next
            pos += 1
        tmp = current.next
        current.next = current.next.next
        current.next.prev = current
        return tmp

def main():
    dll = DoublyLinkedList()
    seven = Node(7)
    dll.head = seven
    dll.traversal()
    ten = Node(10)
    ten.prev = dll.head
    dll.head.next = ten
    two = Node(2)
    two.prev = ten
    ten.next = two
    dll.traversal()
    dll.backward_traversal()
    dll.insertAtBeginning(4)
    dll.insertAtBeginning(5)
    dll.traversal()
    dll.backward_traversal()
    dll.insertAtEnd(6)
    dll.insertAtEnd(9)
    dll.traversal()
    dll.backward_traversal()
    dll.insertAtPosition(11, 2)
    dll.insertAtEnd(12)
    dll.traversal()
    dll.deleteAtBeginning()
    dll.traversal()
    dll.deleteAtEnd()
    dll.traversal()
    dll.deleteAtPosition(2)
    dll.traversal()
    dll.backward_traversal()
    
main()
    
