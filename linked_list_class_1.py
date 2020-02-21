class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = None

    def preppend(self, new_data):
        if not self.head:
            self.head = Node(data=new_data)
            return
        self.head = Node(data=new_data, next=self.head)

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
        while cur:
            cur_list.append(cur.data)
            cur = cur.next
        print(cur_list)

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
            if idx == index:
                print(cur.data)
                return cur
            cur = cur.next
            idx += 1
        return None

    def erase(self, index:int):
        cur = self._find(index)
        if cur:
            if cur.prev:
                cur.prev.next = cur.next
            if cur.next:
                cur.next.prev = cur.prev
            if cur == self.head:
                self.head = cur.next
        else:
            print("Enter correct index")

    def insert(self, new_data, index:int):
        if index >= self._lenght():
            print("Index out of range")
            return
        idx = 0
        cur = self._find(index)
        if cur:
            if not cur.prev:
                self.preppend(new_data)
            if not cur.next:
                cur.next = Node(new_data, prev=cur)
            if cur:
                cur.prev.next = Node(new_data, next=cur, prev=cur.prev)
                cur.prev = cur.prev.next
        else:
            return

    def get_reversed(self):
        cur_list = []
        cur = self.head
        while cur:
            cur_list.append(cur.data)
            cur = cur.next
        return cur_list[::-1]

    def reverse_list(self):
        cur = self.head
        while cur:
            cur_prev = cur.prev
            cur.prev = cur.next
            cur.next = cur_prev
            cur = cur.prev
        self.head = cur_prev.prev # Визуализировать этот код на бумаге.
