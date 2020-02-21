class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self, new_data):
        self.head = Node(new_data) if new_data else None

    def prepend(self, new_data):
        if not self.head:
            self.head = Node(data=new_data)
            return
        self.head = Node(data=new_data, next=self.head)
        self.head.next.prev = self.head

    def append(self, new_data):
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = Node(data=new_data, prev=curr_node)

    def len(self):
        total = 0
        curr_node = self.head
        while curr_node:
            total += 1
            curr_node = curr_node.next
        return total

    def _find(self, index:int):
        idx = 0
        if idx == index:
            return self.head
        curr_node = self.head
        while curr_node:
            if idx == index:
                return curr_node
            idx += 1
            curr_node = curr_node.next
        return None

    def get_by_index(self, index):
        curr = self._find(index)
        if curr:
            print(curr.data)
            return curr.data
        print("Index out of range.")

    def get_by_key(self, key):
        curr = self.head
        while curr:
            if curr.data == key:
                print(curr.data)
                return curr.data

    def insert(self, new_data, index:int):
        index_node = self._find(index)
        if index_node:
            if not index_node.prev:
                self.prepend(new_data)
            else:
                index_node.prev.next = Node(data=new_data, prev=index_node.prev,
                                            next=index_node)
                index_node.prev = index_node.prev.next
        else:
            print("Index out of the range.")

    def erase_by_index(self, index):
        target = self._find(index)
        if target:
            self._remove_element(target)
        else:
            print("index out of range")

    def erase_by_key(self, key):
        curr_node = self.head
        while curr_node:
            if curr_node.data == key:
                self._remove_element(curr_node)
                return
            curr_node = curr_node.next
        print("Data was not found.")

    def _remove_element(self, node):
        target = node
        if not target.prev:
            self.head.next.prev = None
            self.head = self.head.next
        elif not target.next:
            target.prev.next = None
            target.prev = None
        else:
            target.prev.next, target.next.prev = target.next, target.prev

    def reverse_list(self):
        curr_node = self.head
        while curr_node:
            prev_node = curr_node.prev
            curr_node.prev = curr_node.next
            curr_node.next = prev_node
            curr_node = curr_node.prev
        self.head = curr_node.prev.prev

    def display(self):
        display_list = []
        curr_node = self.head
        while curr_node:
            display_list.append(curr_node.data)
            curr_node = curr_node.next
        print(display_list)

