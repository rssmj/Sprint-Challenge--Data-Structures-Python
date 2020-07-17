class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
    
        # initialize previous as none and current as head
        previous = None
        current_node = self.head
        # iterate through list
        while current_node != None:
            # next to current
            next = current_node.next_node
            # initial current to previous
            current_node.next_node = previous
            # previous to current
            previous = current_node
            # current to next
            current_node = next
        # head to previous
        self.head = previous
        