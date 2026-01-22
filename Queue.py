class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        
class Queue:
    def __init__(self):
        self.front= None
        self.rear = None
        
    def is_empty(self):
        return self.front == None
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node
        
    def dequeue(self):
        if self.is_empty():
            return Node(None)
        tmp = self.front
        if self.front.next == None:
            self.front = None
            self.rear = None
            return tmp
        self.front = self.front.next
        tmp.next = None
        return tmp
    
    def front(self):
        return self.front
        
    def printQueue(self):
        current = self.front
        while current != None:
            print(current.data, end = " -> ")
            current = current.next
        print("None")
    
def main():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.printQueue()
    q.dequeue()
    q.printQueue()
    
main()