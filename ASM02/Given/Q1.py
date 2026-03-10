class Order:
    def __init__(self, order_id=None, customer_name=None, total_price=None):
        self.order_id = order_id
        self.customer_name = customer_name
        self.total_price = total_price

    def __str__(self):
        return f"{self.order_id}, {self.customer_name}, {self.total_price}"


class Node:
    def __init__(self, info):
        self.info = info
        self.next = None


class TreeNode:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None


class OrderQueue:
    def __init__(self):
        self.front = None
        self.length = 0

    def isEmpty(self):
        return self.length == 0

    def loadData(self, file_path, size):
        data = read_file(file_path)
        for i in range(size):
            self.enqueue(data[3*i], data[3*i+1], data[3*i+2])

    def enqueue(self, order_id, customer_name, total_price):
        new_node = Node(Order(order_id, customer_name, total_price))
        # ===============================
        # start your code

        # end your code

    def remove(self, id):
        # ===============================
        # start your code

        # end your code

    def display(self):
        print("Order Queue:")
        if self.front is None:
            print("Empty")
        current = self.front
        while current:
            print(current.info.order_id + str(", ") + str(current.info.customer_name) + str(", ") + str(current.info.total_price))
            current = current.next
        print("=========")


class OrderTree:
    def __init__(self):
        self.root = None

    def insert(self, order):
        self.root = self._insert(self.root, order)

    def _insert(self, root, order):
        # ===============================
        # start your code

        # end your code

    def search(self, id):
        return self._search(self.root, id)

    def _search(self, root, id):
        # ===============================
        # start your code

        # end your code

    def remove(self, id):
        self.root = self._remove(self.root, id)

    def _remove(self, root, id):
        # ===============================
        # start your code

        # end your code

    def findMax(self):
        return self._findMax(self.root)

    def _findMax(self, root):
        # ===============================
        # start your code

        # end your code

    def display(self):
        print("Order Tree:")
        stack = list()
        current = self.root
        while current is not None or len(stack) != 0:
            while current is not None:
                stack.append(current)
                current = current.left
            current = stack.pop()
            print(current.info.order_id + str(", ") + str(current.info.customer_name) + str(", ") + str(
                current.info.total_price))
            current = current.right
        print("=========")

    def loadData(self, file_path, size):
        data = read_file(file_path)
        for i in range(size):
            new_order = Order(data[3 * i], data[3 * i + 1], data[3 * i + 2])
            self.insert(new_order)


class ComputerStore:
    def __init__(self):
        self.order_queue = OrderQueue()
        self.order_tree = OrderTree()

    def load(self, file_path, m):
        self.order_queue.loadData(file_path, m)
        self.order_tree.loadData(file_path, m)

    def display(self):
        self.order_queue.display()
        self.order_tree.display()

    # This function is used for Question 1
    def f1(self, file_path, m):
        self.load(file_path, m)
        self.display()

    def f2(self, search_id):
        found = Order()
        # ===============================
        # start your code

        # end your code
        return found
    def f3(self):
        max = Order()
        # ===============================
        # start your code

        # end your code
        return max

    def f4(self, delete_id):
        # ===============================
        # start your code

        # end your code


def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    orders = eval(lines[0].strip())
    return orders


# ========================DO NOT EDIT GIVEN STATEMENTS IN THE MAIN FUNCTION.============================
# ===IF YOU CHANGE, THE GRADING SOFTWARE CAN NOT FIND THE OUTPUT RESULT TO SCORE, THUS THE MARK IS 0.===
def main():
    ds = ComputerStore()
    m = int(input("Input the size of inventory (from 1 to 10):\nm =   "))
    while (m < 1 or m > 10):
        m = int(input("Please input the size of inventory (from 1 to 10):\nm =   "))

    file_path = input("Please input file name (ex: data.txt):  ")

    print("Do you want to run Q1?")
    print("1. Run f1()")
    print("2. Run f2()")
    print("3. Run f3()")
    print("4. Run f4()")
    n = int(input("Input a question (1=>4) : "))
    if n == 1:
        print("OUTPUT:")
        ds.f1(file_path, m)

    if n == 2:
        ds.load(file_path, m)
        search_id = str(input("Search ID: "))
        print("OUTPUT:")
        ds.display()
        found = ds.f2(search_id)
        print("Search Result:")
        if found is not None:
            print(found.order_id + str(", ") + str(found.customer_name) + str(", ") + str(
                found.total_price))
        else:
            print("Not found")

    if n == 3:
        ds.load(file_path, m)
        print("OUTPUT:")
        ds.display()
        max = ds.f3()
        print("Highest Alphabetical ID order: ")
        print(max.order_id + str(", ") + str(max.customer_name) + str(", ") + str(
                max.total_price))

    if n == 4:
        ds.load(file_path, m)
        delete_id = str(input("Delete ID: "))
        print("OUTPUT:")
        print("Before")
        ds.display()
        ds.f4(delete_id)
        print("After")
        ds.display()


# End main
# --------------------------------
if __name__ == "__main__":
    main()
# ================================

