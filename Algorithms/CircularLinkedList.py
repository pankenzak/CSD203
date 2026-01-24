class Node():
    def __init__(self, value):
        self.data = value
        self.next = None
        
class CircularLinkedList:
    def __init__(self):
        self.tail = None
        
    def traversal(self):
        if self.tail is None:
            print("List is empty")
            return
        current = self.tail.next
        head = self.tail.next
        while True:
            print(current.data, end = " -> ")
            current = current.next
            if current == head:
                break
        print(head.data)

    def insertAtBeginning(self, value):
        new_node = Node(value)
        if self.tail is None:
            self.tail = new_node
            new_node.next = self.tail
            return
        old_head = self.tail.next
        self.tail.next = new_node
        new_node.next = old_head
    
    def insertAtEnd(self, value):
        new_node = Node(value)
        if self.tail is None:
            self.tail = new_node
            new_node.next = self.tail
            return
        head = self.tail.next
        self.tail.next = new_node
        new_node.next = head
        self.tail = new_node
        
    def insertAtPosition(self, value, position):
        new_node = Node(value)
        if self.tail is None:
            self.tail = new_node
            new_node.next = self.tail
            return
        current = self.tail.next
        pos = 0
        while pos < position - 1:
            current = current.next
            pos += 1
        new_node.next = current.next
        current.next = new_node
        
    def deleteAtEnd(self):
        if self.tail == None:
            return Node(None)
        current = self.tail.next
        prev = self.tail
        if current == self.tail:
            tmp = self.tail
            self.tail = None     
            return tmp
        while current.next != self.tail:
            current = current.next
        tmp = current.next
        current.next = self.tail.next
        self.tail = current
        return tmp
    
    def deleteAtBeginning(self):
        if self.tail == None:
            return Node(None)
        current = self.tail.next
        if current == self.tail:
            tmp = self.tail
            self.tail = None     
            return tmp
        tmp = self.tail.next
        self.tail.next = self.tail.next.next
        return tmp
    
    def deleteAtPosition(self, position):
        if self.tail == None:
            return Node(None)
        current = self.tail.next
        if current == self.tail:
            tmp = self.tail
            self.tail = None     
            return tmp
        pos = 0
        while pos < position - 1:
            current = current.next
            pos += 1
        tmp = current.next
        current.next = current.next.next
        return tmp
    
    def reverse(self):
        if self.tail is None or self.tail.next == self.tail:
            return
        prev = self.tail
        head = self.tail.next
        current = head
        
        old_head = head
        while True:
            next_node = current.next
            current.next = prev
            
            prev = current
            current = next_node
            if current == old_head:
                break
        self.tail = old_head

def main():
    cll = CircularLinkedList()
    ten = Node(10)
    cll.tail = ten
    ten.next = ten
    two = Node(2)
    cll.tail = two
    two.next = ten
    ten.next = two
    cll.traversal()
    cll.insertAtBeginning(3)
    cll.insertAtBeginning(4)
    cll.traversal()
    cll.insertAtEnd(5)
    cll.traversal()
    cll.insertAtPosition(6,2)
    cll.insertAtPosition(7,4)
    cll.traversal()
    cll.deleteAtEnd()
    cll.traversal()
    cll.deleteAtBeginning()
    cll.traversal()
    cll.deleteAtPosition(2)
    cll.deleteAtPosition(6)
    cll.traversal()
    cll.reverse()
    cll.traversal()

main()
    
