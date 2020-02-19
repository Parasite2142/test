class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = Node()

    def preppend(self, new_data):
        if not self.head:
            self.head = Node(data=new_data)
            return
        self.head.next = Node(data=new_data, next=self.head.next,
                              prev=self.head)
        self.head.next.prev = self.head

    def append(self, new_data):
        if not self.head:
            self.head = Node(data=new_data)
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node(data=new_data, prev=cur)

    def display(self):
        cur_list = []
        cur = self.head
        while cur.next:
            cur = cur.next
            cur_list.append(cur.data)
        print(cur_list)

    def _new_node(self, new_data):
        if not self.head:
            self.head = Node(data=new_data)
            return

    def _lenght(self):
        total = 0
        cur = self.head
        while cur:
            total +=1
            cur = cur.next
        return total

    def _find(self, index:int):
        if index >= self._lenght():
            print("Index out of range")
            return
        idx = 0
        cur = self.head
        while cur.next:
            cur = cur.next
            if idx == index:
                print(cur.data)
            idx += 1
        return None

    def erase(self, index:int):
        if index >= self._lenght():
            print("Index out of range")
            return
        cur = self._find(index)
        if cur:
            if cur.prev:
                cur.prev.next = cur.next
            if cur.next:
                cur.next.prev = cur.prev
            if cur == self.head:
                self.head = cur.next

my_list = LinkedList()

my_list.preppend(3)
my_list.preppend(2)
my_list.preppend(1)
my_list.append(4)
my_list.append(5)

my_list.display()

my_list._find(3)

my_list.display()

