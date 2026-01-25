class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        
class Stack:
    def __init__(self):
        self.top = None
        
    def is_empty(self):
        if self.top == None:
            return True
        else:
            return False
        
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        
    def pop(self):
        if self.is_empty():
            return Node(None)
        tmp = self.top
        self.top = self.top.next
        tmp.next = None
        return tmp
    
    def peek(self):
        return self.top
    
    def printStack(self):
        current = self.top
        while current != None:
            print(current.data, end = " -> ")
            current = current.next
        print("None")
        
def main():
    s = Stack()
    s.push(1)
    s.push(2)
    s.pop()
    if s.is_empty():
        print("The stack is empty")
        return
    else:
        s.printStack()
    s.push(3)
    s.push(7)
    s.push(9)
    s.pop()
    s.printStack()
    s.peek()

main()
