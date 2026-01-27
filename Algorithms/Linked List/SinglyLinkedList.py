class Node:
    #Constructor
    def __init__(self, value):
        self.data = value
        self.next = None
        
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        
    def length(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.next
        return count
    
    def traversal(self):
        current = self.head
        while current != None:
            print(current.data, end= " -> ")
            current = current.next
        print("None")
        
    def insertAtBeginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        
    def insertAtEnd(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node
        
    def insertAtPosition(self, value, position):
        new_node = Node(value)
        pos = 0
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        if position <= 0:
            new_node.next = self.head
            self.head = new_node

        else:
            while pos < position - 1:
                if current.next is None:
                    break
                else:
                    current = current.next
                    pos += 1
            new_node.next = current.next
            current.next = new_node
            
    def deleteAtBeginning(self):
        if self.head == None:
            print("List is empty. Cannot delete")
            return Node(None)
        tmp = self.head
        self.head = self.head.next
        tmp.next = None
        return tmp

    def deleteAtEnd(self):
        if self.head == None:
            print("List is empty. Cannot delete")
            return Node(None)
        current = self.head
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
        return tmp
    
    def rec_traversal(self, current):
        if current == None:
            print("None")
            return
        print(current.data, end = " -> ")
        self.rec_traversal(current.next)
        return

    def rec_length(self, count, current):
        if current == None:
            return count
        result = self.rec_length(count + 1, current.next)
        return result

def main():
    sll = SinglyLinkedList()
    seven = Node(7)
    sll.head = seven
    ten = Node(10)
    sll.head.next = ten
    two = Node(2)
    ten.next = two
    sll.traversal()
    sll.insertAtBeginning(12)
    sll.insertAtBeginning(15)
    sll.traversal()
    sll.insertAtEnd(4)
    sll.traversal()
    sll.insertAtPosition(8, 1)
    sll.traversal()
    sll.deleteAtBeginning()
    sll.traversal()
    sll.deleteAtEnd()
    sll.traversal()
    sll.deleteAtPosition(-1)
    sll.traversal()
    sll.rec_traversal(sll.head)
    print(sll.length())
    print(sll.rec_length(0, sll.head))

main()