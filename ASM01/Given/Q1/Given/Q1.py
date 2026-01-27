class Node:                                  # lớp Node
    def __init__(self, data):
        self.data = data                     # giá trị node
        self.prev = None                     # trỏ về node trước
        self.next = None                     # trỏ đến node sau


class DoublyLinkedList:                      # danh sách liên kết đôi
    def __init__(self):
        self.head = None                     # node đầu
        self.tail = None                     # node cuối


    # 1. Thêm vào đầu danh sách
    def addToHead(self, x):
        newNode = Node(x)
        if self.head is None:
            self.head = self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode


    # 2. Thêm vào cuối danh sách
    def addToTail(self, x):
        newNode = Node(x)
        if self.tail is None:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode


    # 3. Thêm x sau node p
    def addAfter(self, p, x):
        if p is None:
            return
        newNode = Node(x)
        newNode.next = p.next
        newNode.prev = p
        if p.next:
            p.next.prev = newNode
        else:
            self.tail = newNode
        p.next = newNode


    # 4. Duyệt và in danh sách
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


    # 5. Xóa node đầu
    def deleteFromHead(self):
        if self.head is None:
            return None
        value = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return value


    # 6. Xóa node cuối
    def deleteFromTail(self):
        if self.tail is None:
            return None
        value = self.tail.data
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        return value


    # 7. Xóa node sau p
    def deleteAfter(self, p):
        if p is None or p.next is None:
            return None
        temp = p.next
        value = temp.data
        p.next = temp.next
        if temp.next:
            temp.next.prev = p
        else:
            self.tail = p
        return value


    # 8. Xóa node có giá trị x
    def delValue(self, x):
        current = self.head
        while current:
            if current.data == x:
                self.delNode(current)
                return True
            current = current.next
        return False


    # 9. Tìm VỊ TRÍ (index) của node có giá trị x
    def searchIndex(self, x):
        current = self.head
        index = 0
        while current:
            if current.data == x:
                return index
            current = current.next
            index += 1
        return -1


    # (phụ) Tìm NODE có giá trị x
    def searchNode(self, x):
        current = self.head
        while current:
            if current.data == x:
                return current
            current = current.next
        return None


    # 10. Đếm số node
    def count(self):
        c = 0
        current = self.head
        while current:
            c += 1
            current = current.next
        return c


    # 11. Xóa node tại vị trí i
    def delAt(self, i):
        if i < 0:
            return
        current = self.head
        index = 0
        while current:
            if index == i:
                self.delNode(current)
                return
            index += 1
            current = current.next


    # 12. Sắp xếp tăng dần
    def sort(self):
        i = self.head
        while i:
            j = i.next
            while j:
                if i.data > j.data:
                    i.data, j.data = j.data, i.data
                j = j.next
            i = i.next


    # 13. Xóa node p
    def delNode(self, p):
        if p is None:
            return
        if p.prev:
            p.prev.next = p.next
        else:
            self.head = p.next
        if p.next:
            p.next.prev = p.prev
        else:
            self.tail = p.prev


    # 14. Chuyển sang mảng
    def toArray(self):
        arr = []
        current = self.head
        while current:
            arr.append(current.data)
            current = current.next
        return arr


    # 15. Gộp hai danh sách đã sắp xếp
    def merge(self, other):
        result = DoublyLinkedList()
        a = self.head
        b = other.head
        while a and b:
            if a.data <= b.data:
                result.addToTail(a.data)
                a = a.next
            else:
                result.addToTail(b.data)
                b = b.next
        while a:
            result.addToTail(a.data)
            a = a.next
        while b:
            result.addToTail(b.data)
            b = b.next
        return result


    # 16. Thêm x trước node p
    def addBefore(self, p, x):
        if p is None:
            return
        newNode = Node(x)
        newNode.next = p
        newNode.prev = p.prev
        if p.prev:
            p.prev.next = newNode
        else:
            self.head = newNode
        p.prev = newNode


    # 17. Nối danh sách other vào cuối
    def attach(self, other):
        if self.tail:
            self.tail.next = other.head
            if other.head:
                other.head.prev = self.tail
            self.tail = other.tail
        else:
            self.head = other.head
            self.tail = other.tail


    # 18. Giá trị lớn nhất
    def max(self):
        if self.head is None:
            return None
        m = self.head.data
        current = self.head.next
        while current:
            if current.data > m:
                m = current.data
            current = current.next
        return m


    # 19. Giá trị nhỏ nhất
    def min(self):
        if self.head is None:
            return None
        m = self.head.data
        current = self.head.next
        while current:
            if current.data < m:
                m = current.data
            current = current.next
        return m


    # 20. Tổng các phần tử
    def sum(self):
        s = 0
        current = self.head
        while current:
            s += current.data
            current = current.next
        return s


    # 21. Trung bình
    def avg(self):
        if self.count() == 0:
            return 0
        return self.sum() / self.count()


    # 22. Kiểm tra đã sắp xếp chưa
    def isSorted(self):
        current = self.head
        while current and current.next:
            if current.data > current.next.data:
                return False
            current = current.next
        return True


    # 23. Chèn x đúng vị trí
    def insert(self, x):
        if self.head is None or x <= self.head.data:
            self.addToHead(x)
            return
        current = self.head
        while current.next and current.next.data < x:
            current = current.next
        self.addAfter(current, x)


    # 24. Đảo ngược danh sách
    def reverse(self):
        current = self.head
        while current:
            current.prev, current.next = current.next, current.prev
            current = current.prev
        self.head, self.tail = self.tail, self.head


    # 25. So sánh hai danh sách
    def equals(self, other):
        a = self.head
        b = other.head
        while a and b:
            if a.data != b.data:
                return False
            a = a.next
            b = b.next
        return a is None and b is None
    
def main():
    dll = DoublyLinkedList()

    dll.addToHead(10)
    print("(1) addToHead – Thêm một phần tử 10 ĐẦU danh sách:", end=" ")
    dll.traverse()

    dll.addToHead(11)
    print("(1) addToHead – Thêm một phần tử 11 ĐẦU danh sách:", end=" ")
    dll.traverse()

    dll.addToTail(20)
    print("(2) addToTail – Thêm một phần tử 20 CUỐI danh sách:", end=" ")
    dll.traverse()

    dll.addToTail(27)
    print("(2) addToTail – Thêm một phần tử 27 CUỐI danh sách:", end=" ")
    dll.traverse()

    print("(9) searchIndex – Vị trí của node có giá trị 10:", dll.searchIndex(10))

    p = dll.searchNode(10)
    dll.addAfter(p, 15)
    print("(3) addAfter – Thêm phần tử 15 SAU node có giá trị 10:", end=" ")
    dll.traverse()

    print("(4) traverse – Duyệt và in toàn bộ danh sách:", end=" ")
    dll.traverse()

    print("(5) deleteFromHead – Xóa phần tử ở ĐẦU danh sách:", dll.deleteFromHead())
    print("(6) deleteFromTail – Xóa phần tử ở CUỐI danh sách:", dll.deleteFromTail())

    p = dll.searchNode(15)
    print("(7) deleteAfter – Xóa node đứng SAU node có giá trị 15:", dll.deleteAfter(p))
    print("Danh sách hiện tại:", end=" ")
    dll.traverse()

    dll.addToTail(5)
    print("(2) addToTail – Thêm phần tử 5 vào cuối:", end=" ")
    dll.traverse()

    dll.addToTail(25)
    print("(2) addToTail – Thêm phần tử 25 vào cuối:", end=" ")
    dll.traverse()

    print("(8) delValue – Xóa node có GIÁ TRỊ bằng 5:", dll.delValue(5))
    print("(10) count – Đếm số lượng node trong danh sách:", dll.count())

    dll.addToTail(30)
    print("(2) addToTail – Thêm phần tử 30 vào cuối:", end=" ")
    dll.traverse()

    dll.addToTail(12)
    print("(2) addToTail – Thêm phần tử 12 vào cuối:", end=" ")
    dll.traverse()

    dll.delAt(1)
    print("(11) delAt – Xóa node tại vị trí index = 1:", end=" ")
    dll.traverse()

    dll.sort()
    print("(12) sort – Sắp xếp danh sách theo thứ tự TĂNG DẦN:", end=" ")
    dll.traverse()

    node = dll.searchNode(12)
    dll.delNode(node)
    print("(13) delNode – Xóa TRỰC TIẾP node có giá trị 12:", end=" ")
    dll.traverse()

    print("(14) toArray – Chuyển danh sách liên kết sang mảng:", dll.toArray())

    dll2 = DoublyLinkedList()
    dll2.addToTail(1)
    dll2.addToTail(40)

    merged = dll.merge(dll2)
    print("(15) merge – GỘP hai danh sách đã sắp xếp:", merged.toArray())

    p = merged.searchNode(40)
    merged.addBefore(p, 35)
    print("(16) addBefore – Thêm 35 vào TRƯỚC node có giá trị 40:", end=" ")
    merged.traverse()

    merged.attach(dll2)
    print("(17) attach – NỐI danh sách thứ hai vào CUỐI danh sách hiện tại:", end=" ")
    merged.traverse()

    print("(18) max – Tìm GIÁ TRỊ LỚN NHẤT trong danh sách:", merged.max())
    print("(19) min – Tìm GIÁ TRỊ NHỎ NHẤT trong danh sách:", merged.min())
    print("(20) sum – Tính TỔNG các phần tử trong danh sách:", merged.sum())
    print("(21) avg – Tính GIÁ TRỊ TRUNG BÌNH các phần tử:", merged.avg())

    print("(22) isSorted – Kiểm tra danh sách có được SẮP XẾP hay không:", merged.isSorted())

    merged.insert(22)
    print("(23) insert – Chèn giá trị 22 vào ĐÚNG VỊ TRÍ:", end=" ")
    merged.traverse()

    merged.reverse()
    print("(24) reverse – ĐẢO NGƯỢC thứ tự danh sách:", end=" ")
    merged.traverse()

    print("(25) equals – So sánh hai danh sách có GIỐNG NHAU không:", merged.equals(dll))


main()

