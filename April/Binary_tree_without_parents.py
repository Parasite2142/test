class BinaryTree:
    class Node:
        def __init__(self, value):
            self.value = value
            self.right = None
            self.left = None

    def __init__(self, data=None):
        self.head = self.Node(value=data)
        self.length = 0

    def add(self, value):
        if not self.head:
            self.head = value
        else:
            curr_node = self.head
            last_node = None
            while curr_node or last_node:
                if not curr_node:
                    if last_node.value == value:
                        print('Duplicated value')
                    if last_node.value > value and not last_node.left:
                        last_node.left = self.Node(value=value)
                        return
                    else:
                        last_node.right = self.Node(value=value)
                        return
                if curr_node.value > value:
                    last_node = curr_node
                    curr_node = curr_node.left
                else:
                    last_node = curr_node
                    curr_node = curr_node.right

    def __contains__(self, value):
        if not self.head:
            return None
        curr_node = self.head
        while curr_node:
            if curr_node.value == value:
                print(value)
            if curr_node.value > value:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right

    def remove(self, value):
        if not self.head:
            return None
        if self.head.value == value:
            if not self.head.right and self.head.left:
                self.head.value = None
                return value
            if not self.head.right:
                self.head = self.head.left
                return value
            if not self.head.left:
                self.head = self.head.right
                return value
            else:
                self._look_lowest_leaf(self.head)
                return value
        curr_node = self.head
        last_node = self.head
        while curr_node:
            if curr_node.value == value:
                if curr_node.value < last_node.value:
                    if not curr_node.left and curr_node.right:  # del if leaf
                        last_node.left = None
                        return value
                    if curr_node.right and curr_node.left:
                        last_node.left = self._look_lowest_leaf(
                            node=curr_node.right, last=curr_node)
                        last_node.left.right = curr_node.right
                        last_node.left.left = curr_node.left
                        return
                    elif curr_node.right and not curr_node.left:
                        last_node.left = curr_node.right
                        return
                    elif curr_node.left and not curr_node.right:
                        last_node.left = curr_node.left
                        return
            if curr_node.value > value:
                last_node = curr_node
                curr_node = curr_node.left
            else:
                last_node = curr_node
                curr_node = curr_node.right
        raise ValueError

    def _look_lowest_leaf(self, node, last=None):
        curr_node = node
        last_node = last
        while curr_node:
            if not curr_node.left:
                last_node.left = None
                return curr_node
            last_node = curr_node
            curr_node = curr_node.left
