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
        result = self.find(index)
        if not result.prev:
            self.prepend(new_data)
        elif result:
            result.prev.next = Node(data=new_data, next=result,
                                    prev=result.prev)
            result.prev = result.prev.next
        else:
            print("Index out of the range")

    def _remove_element(self, target_node):
        target = target_node
        if not target.next:
            target.prev.next = None
            target = None
        elif not target.prev:
            self.head = target.next
            self.head.prev = None
            target = None
        elif target:
            target.prev.next = target.next
            target.next.prev = target.prev.prev
            target = None

    def erase_by_index(self, index:int):
        target = self.find(index)
        if target:
            self._remove_element(target)


    def erase_by_key(self, key):
        current_node = self.head
        while current_node:
            if key == current_node.data:
                self._remove_element(current_node)
                return
            current_node = current_node.next
        print("Data was not found.")

    def get_list(self):
        display_list = []
        current_node = self.head
        while current_node:
            display_list.append(current_node.data)
            current_node = current_node.next
        print(display_list)

    def get_index(self, key):
        current_node = self.head
        idx = 0
        while current_node:
            if current_node.data == key:
                return idx
            idx+=1
            current_node = current_node.next
        print("Data was not found.")

    def reverse_list(self):
        current_node = self.head
        while current_node:
            prev_node = current_node.prev
            current_node.prev = current_node.next
            current_node.next = prev_node
            current_node = current_node.prev
        self.head = prev_node.prev

