class SoftDrink:
    def __init__(self, code, make, unit, volume, price):
        self.code = code
        self.make = make
        self.unit = unit
        self.volume = volume
        self.price = price
    
    def __repr__(self):
        return f"{self.code}, {self.make}, {self.unit}, {self.volume}, {'%.3f' % self.price}"

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get_node(self, index):
        current = self.head
        for i in range(index):
            if current is None:
                return None
            current = current.next
        return current
    
    def addLast(self, code, make, unit, volume, price):
        new_node = Node(SoftDrink(code, make, unit, volume, price))
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

	# def addFirst(self, code, make, unit, volume, price):
		# ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------
        
		
		
        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------	
    
    # def addAfter(self, second_node, new_node):
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------
        
		
		
        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------	
    
    
    # def sortByPrice(self):
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------
        
		
		
        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------

    def display(self):
        current = self.head
        while current:
            print(current.data, end = ' ')
            current = current.next
            print()

    def loadData(self):
        self.addLast('PS021', 'Pepsi', 'Carton of 24 bottles', '390ml', 175.0)
        self.addLast('MD033', 'Mirinda', 'Carton of 24 cans', '320ml', 168.0)
        self.addLast('SP005', 'Schweppes', 'Carton of 24 cans', '320ml', 220.0)
        self.addLast('2C017', 'Coca-Cola', 'Carton of 24 bottles', '600ml', 218.0)
        self.addLast('MD020', 'Mirinda', 'Carton of 24 bottles', '390ml', 175.0)
    
    # This function is used for Question 1
    def f1(self):
        """
            Question 1: Insert at the beginning of the current list a new SoftDrink 
            which code = '7U019', make = '7-Up', unit = 'Carton of 24 cans', volume 
            = '320ml', price = 168.0. Hint: 
                (1) Implement an 'addFirst' function that inserts a new SoftDrink 
                    into the current list's head.
                (2) Call the 'addFirst' function in the f1() to perform it.
            With the data provided, the output after running this function will be:
                OUTPUT:
                7U019, 7-Up, Carton of 24 cans, 320ml, 168.000 
                PS021, Pepsi, Carton of 24 bottles, 390ml, 175.000 
                MD033, Mirinda, Carton of 24 cans, 320ml, 168.000 
                SP005, Schweppes, Carton of 24 cans, 320ml, 220.000 
                2C017, Coca-Cola, Carton of 24 bottles, 600ml, 218.000 
                MD020, Mirinda, Carton of 24 bottles, 390ml, 175.000 
        """
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------
        
		
		
        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.display()

    # This function is used for Question 2
    def f2(self):
        # Initialize a new node that will be used in Question 2
        new_node = Node(SoftDrink('SR007', 'Sprite', 'Carton of 24 bottles', '390ml', 112.0))
        """
            Question 2: Using the new_node initialized above, write your code to insert 
            the new_node after the second node (which index is 1) of the current list.
            Hint: 
                (1) Use the 'get_node' function given in this file to find the 
                    second_node (which index is 1).
                (2) Implement an 'addAfter' function with 2 parameters new_node, 
                    second_node above to insert new_node after second_node.
				(3)	Call the 'addAfter' function in the f2() to perform it.
            With the data provided, the output after running this function will be:
                OUTPUT:
                PS021, Pepsi, Carton of 24 bottles, 390ml, 175.000
                MD033, Mirinda, Carton of 24 cans, 320ml, 168.000
                SR007, Sprite, Carton of 24 bottles, 390ml, 112.000
                SP005, Schweppes, Carton of 24 cans, 320ml, 220.000
                2C017, Coca-Cola, Carton of 24 bottles, 600ml, 218.000
                MD020, Mirinda, Carton of 24 bottles, 390ml, 175.000
        """
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------
        
		
		
        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.display()

    # This function is used for Question 3
    def f3(self):
        """
            Question 3: Find the first node in the linked list that has SoftDrink's make 
            start with 'M', if such a node is found, then set the price of SoftDrink in 
            this node to 159.0. Hint: 
                (1) Use str.startswith(start) to find the first node in a linked list 
                    whose SoftDrink's make begins with 'M'
                (2) Update the node's SoftDrink price to 159.0   
            Example: if the linked list before change is  
                OUTPUT:
                PS021, Pepsi, Carton of 24 bottles, 390ml, 175.000
                MD033, Mirinda, Carton of 24 cans, 320ml, 168.000
                SP005, Schweppes, Carton of 24 cans, 320ml, 220.000
                2C017, Coca-Cola, Carton of 24 bottles, 600ml, 218.000
                MD020, Mirinda, Carton of 24 bottles, 390ml, 175.000
            then the the linked list after change is:  
                OUTPUT:
                PS021, Pepsi, Carton of 24 bottles, 390ml, 175.000
                MD033, Mirinda, Carton of 24 cans, 320ml, 159.000
                SP005, Schweppes, Carton of 24 cans, 320ml, 220.000
                2C017, Coca-Cola, Carton of 24 bottles, 600ml, 218.000
                MD020, Mirinda, Carton of 24 bottles, 390ml, 175.000
        """
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------        
        
		
		
        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.display()

    # This function is used for Question 4
    def f4(self):
        """
            Question 4: Sort the linked list in an ascending order according to 
            SoftDrink's code. Hint: 
                Create a new function 'sortByPrice' to sort the linked list, then call 
                the created function in the f4() to perform it.
            Example: if the linked list before change is  
                OUTPUT:
                PS021, Pepsi, Carton of 24 bottles, 390ml, 175.000
                MD033, Mirinda, Carton of 24 cans, 320ml, 168.000
                SP005, Schweppes, Carton of 24 cans, 320ml, 220.000
                2C017, Coca-Cola, Carton of 24 bottles, 600ml, 218.000
                MD020, Mirinda, Carton of 24 bottles, 390ml, 175.000
            then the the linked list after change is:  
                OUTPUT:
                2C017, Coca-Cola, Carton of 24 bottles, 600ml, 218.000
                MD020, Mirinda, Carton of 24 bottles, 390ml, 175.000
                MD033, Mirinda, Carton of 24 cans, 320ml, 168.000
                PS021, Pepsi, Carton of 24 bottles, 390ml, 175.000
                SP005, Schweppes, Carton of 24 cans, 320ml, 220.000                   
        """
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------        
        
		
		
        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.display()

    # This function is used for Question 5
    def f5(self):
        """
            Question 5: Delete the first node in the linked list with SoftDrink's 
            volume = '390ml'.
            Example: if the linked list before change is  
                OUTPUT:
                PS021, Pepsi, Carton of 24 bottles, 390ml, 175.000
                MD033, Mirinda, Carton of 24 cans, 320ml, 168.000
                SP005, Schweppes, Carton of 24 cans, 320ml, 220.000
                2C017, Coca-Cola, Carton of 24 bottles, 600ml, 218.000
                MD020, Mirinda, Carton of 24 bottles, 390ml, 175.000
            then the the linked list after change is:  
                OUTPUT:
                MD033, Mirinda, Carton of 24 cans, 320ml, 168.000
                SP005, Schweppes, Carton of 24 cans, 320ml, 220.000
                2C017, Coca-Cola, Carton of 24 bottles, 600ml, 218.000
                MD020, Mirinda, Carton of 24 bottles, 390ml, 175.000                         
        """
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------        
        
		
		
        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.display()

# ========================DO NOT EDIT GIVEN STATEMENTS IN THE MAIN FUNCTION.============================
# ===IF YOU CHANGE, THE GRADING SOFTWARE CAN NOT FIND THE OUTPUT RESULT TO SCORE, THUS THE MARK IS 0.===
def main():
    lst = LinkedList()
    lst.loadData()
    print("Do you want to run Q1?")
    print("1. Run f1()")
    print("2. Run f2()")
    print("3. Run f3()")
    print("4. Run f4()")
    print("5. Run f5()")

    n = int(input("Enter a number : "))

    if n == 1:
        print("OUTPUT:")
        lst.f1()

    if n ==2:
        print("OUTPUT:")
        lst.f2()

    if n == 3:
        print("OUTPUT:")
        lst.f3()

    if n == 4:
        print("OUTPUT:")
        lst.f4()

    if n == 5:
        print("OUTPUT:")
        lst.f5()
# End main
# --------------------------------
if __name__ == "__main__":
    main()
# ============================================================
