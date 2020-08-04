class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

    def get_prev(self):
        return self.prev

    def set_prev(self, new_prev):
        self.prev = new_prev

    def __str__(self):
        return f"{self.value}"


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        new_node = ListNode(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next(self.head)
            self.head.set_prev(new_node)
            self.head = new_node
        self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        if self.length == 0:
            return None
        removed_node = self.head.get_value()
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.get_next()
            self.head.prev = None
        self.length -= 1
        return removed_node

    """
    Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        new_node = ListNode(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.set_next(new_node)
            self.tail = new_node
        self.length += 1

    """
    Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        if self.length == 0:
            return None

        removed_node = self.tail.get_value()
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.get_prev()
            self.tail.next = None
        self.length -= 1
        return removed_node

    """
    Removes the input node from its current spot in the
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        if node is self.head:
            return None
        self.delete(node)
        self.add_to_head(node.value)

    """
    Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        if node is self.tail:
            return None
        self.delete(node)
        self.add_to_tail(node.get_value())

    """
    Deletes the input node from the List, preserving the
    order of the other elements of the List.
    """

    def delete(self, node):
        if self.length == 0:
            return None

        elif node == self.head:
            return self.remove_from_head()

        elif node == self.tail:
            return self.remove_from_tail()

        else:
            current = self.head
            while current.next is not None:
                if current == node:
                    current.prev.set_next(current.get_next())
                    current.next.set_prev(current.get_prev())
                    self.length -= 1
                    return current.get_value()
                current = current.get_next()
        return None
    """
    Finds and returns the maximum value of all the nodes
    in the List.
    """

    def get_max(self):
        if self.length == 0:
            return None
        else:
            current_node = self.head
            maximum_value = self.head.get_value()
            while current_node is not None:
                if current_node.get_value() > maximum_value:
                    maximum_value = current_node.get_value()
                current_node = current_node.get_next()
            return maximum_value

    """
    Helper method to print out all values in the list
    """

    def print_list(self):
        if self.length == 0:
            return None
        current_node = self.head
        output = ""
        while current_node is not None:
            output += f" {current_node.get_value()} => "
            current_node = current_node.get_next()
        print(output.strip())
