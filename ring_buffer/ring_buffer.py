from doubly_linked_list import DoublyLinkedList


# using a Doubly Linked List for storage
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = DoublyLinkedList()
        self.oldest_node = None

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.oldest_node = self.storage.head
        elif self.storage.length == self.capacity:
            temp = self.oldest_node.get_next()
            self.oldest_node.value = item
            self.oldest_node = temp
            if self.oldest_node is None:
                self.oldest_node = self.storage.head

    def get(self):
        storage_values = []
        current = self.storage.head
        count = 0

        while count < self.storage.length:
            storage_values.append(current.value)
            current = current.get_next()
            count += 1

        return storage_values

# using a list for storage
# # class RingBuffer:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.storage = []
#         self.oldest_index = None

#     def append(self, item):
#         if len(self.storage) < self.capacity:
#             self.storage.append(item)
#             self.oldest_index = 0
#         elif len(self.storage) == self.capacity:
#             self.storage[self.oldest_index] = item
#             self.oldest_index += 1
#             if self.oldest_index == self.capacity:
#                 self.oldest_index = 0

#     def get(self):
#         return self.storage


r = RingBuffer(3)
r.append('a')
r.append('b')
r.append('c')
r.append('d')
r.append('e')
r.append('f')
print(r.get())
