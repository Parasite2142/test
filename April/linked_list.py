class LinkedList:
    class Node:
        def __init__(self, data, next_node=None, prev_node=None):
            self.data = data
            self.next = next_node
            self.prev = prev_node

    def __init__(self, data=None):
        self.head = self.Node(data=data)
        self.tail = None
        self.length = 1 if self.head.data else 0

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        target = self._find_node(index)
        if target:
            return target.data
        else:
            return None

    def prepend(self, new_data):
        if self.length == 0:
            self.head.data = new_data
            self.length += 1
            return
        if self.tail:
            self.head = self.Node(data=new_data, next_node=self.head)
            self.head.next.prev = self.head
            self.length += 1
        else:
            self.head = self.Node(data=new_data, next_node=self.head)
            self.tail = self.head.next
            self.tail.prev = self.head
            self.length += 1

    def append(self, new_data):
        if self.length < 1:
            self.prepend(new_data)
        else:
            if self.tail:
                self.tail.next = self.Node(data=new_data, prev_node=self.tail)
                self.tail = self.tail.next
                self.length += 1
            else:
                self.tail = self.Node(data=new_data, prev_node=self.head)
                self.head.next = self.tail
                self.length += 1

    def insert(self, index, new_data):
        if index == 0:
            self.prepend(new_data)
            return
        elif index == self.length - 1:
            self.append(new_data)
            return
        else:
            curr_node = self._find_node(index)
            new_node = self.Node(
                data=new_data, prev_node=curr_node.prev,
                next_node=curr_node)
            curr_node.prev.next, curr_node.prev = new_node, new_node
            self.length += 1
            return

    def check_range(self, index):
        if index > self.length - 1:
            print('Index out of range')
            return

    def to_list(self):
        xlist = []
        curr_node = self.head
        while curr_node:
            xlist.append(curr_node.data)
            curr_node = curr_node.next
        return xlist

    def _find_node(self, index):
        if not self.check_range(index):
            curr_node = self.head
            for idx in range(self.length):
                if idx == index:
                    return curr_node
                curr_node = curr_node.next

    def pop(self, index=None):
        if self.length > 0:
            if index == self.length - 1 or not index:
                return self._pop_right()
            if index == 0:
                return self.popleft(index)
            else:
                target = self._find_node(index)
                poped = target.data
                target.prev.next = target.next
                target.next.prev = target.prev
                self.length -= 1
                return poped
        else:
            return None

    def _pop_right(self):
        poped = self.tail.data
        if self.tail.prev != self.head:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            self.tail = None
        self.length -= 1
        return poped

    def popleft(self, index):
        if self.length > 0:
            if not index or index == 0:
                poped = self.head.data
                if self.head.next == self.tail:
                    self.head = self.tail
                    self.tail = None
                elif self.head.next != self.tail:
                    self.head = self.head.next
                    self.head.prev = None
                else:
                    self.head.data = None
                self.length -= 1
                return poped
            else:
                return self.pop(index)
        else:
            return None

    def index(self, key):
        curr_node = self.head
        for idx in range(self.length):
            if curr_node.data == key:
                return idx
            curr_node = curr_node.next
        else:
            return None

    def __contains__(self, item):
        if self.index(item):
            return True
        else:
            return False