class Node:
    """Initiates node class for linked list class data_sctructure."""
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class Linked_List:
    """Class to manage linked list."""
    def __init__(self, initial_value=None):
        self.head = Node(initial_value) if initial_value else None

    def prepend(self, new_data):
        """ Method to add new node to the linked list
        at the beginning of the chain. Takes O(1). """
        if not self.head:
            self.head = Node(data=new_data)
            return
        self.head = Node(data=new_data, next=self.head)
        self.head.next.prev = self.head

    def append(self, new_data):
        """ Method to add new node to the linked list
        at the end of the chain. Takes O(n)."""
        if not self.head:
            self.head = Node(data=new_data)
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = Node(data=new_data, prev=current_node)

    def lenght(self):
        """ Method to check the lenght of the chain. """
        total = 0
        current_node = self.head
        while current_node:
            total += 1
            current_node = current_node.next
        return total

    def find(self, index):
        """ Method to check the item on the called index. """
        if index >= self.lenght():
            print("Index of out the range.")
            return
        idx = 0
        current_node = self.head
        while current_node:
            if idx == index:
                return current_node
            idx += 1
            current_node = current_node.next

    def insert(self, new_data, index:int):
        """ Method to add the data between the nodes. """
        if index >= self.lenght():
            print("Index of out the range.")
            return
        result = self.find(index)
        if not result.prev:
            self.prepend(new_data)
            return
        if result:
            result.prev.next = Node(data=new_data, next=result,
                                    prev=result.prev)
            result.prev = result.prev.next
            return

    def erase(self, index:int):
        target = self.find(index)
        if target:
            if not target.next:
                target.prev.next = None
                target = None
                return
            if not target.prev:
                self.head = target.next
                self.head.prev = None
                target = None
                return
            if target:
                target.prev.next = target.next
                target.next.prev = target.prev.prev
                target = None
                return

    def get_list(self):
        display_list = []
        current_node = self.head
        while current_node:
            display_list.append(current_node.data)
            current_node = current_node.next
        print(display_list)

    def reverse_list(self):
        current_node = self.head
        while current_node:
            prev_node = current_node.prev
            current_node.prev = current_node.next
            current_node.next = prev_node
            current_node = current_node.prev
        self.head = prev_node.prev


my_list = Linked_List()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)
my_list.get_list()
my_list.insert(4, 4)
my_list.get_list()

my_list.erase(0)
my_list.insert(0, 0)
my_list.reverse_list()
my_list.get_list()
