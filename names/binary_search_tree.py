class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True

        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)

        if target > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree

    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node

    def for_each(self, fn):
        fn(self.value)

        if self.left is not None:
            self.left.for_each(fn)

        if self.right is not None:
            self.right.for_each(fn)

    def iterative_depth_first_for_each(self, fn):
        # DFT: LIFO
        # we'll use a stack
        stack = []
        stack.append(self)

        while len(stack) > 0:
            # pop the top node from the stack
            current = stack.pop()
            # add the current node's right child first
            if current.right:
                stack.append(current.right)
            # add the current node's left child
            if current.left:
                stack.append(current.left)

            # call anonymous function
            fn(current.value)

    def iterative_breadth_first_for_each(self, fn):
        # BFS: FIFO
        # we'll use a queue to facilitate ordering
        queue = []
        queue.append(self)

        while len(queue) > 0:
            current = queue.pop(0)

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

            fn(current.value)

    def get_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, value):
        if self is None:
            return None

        if value < self.value:
            self.left.delete(value)
        elif value > self.value:
            self.right.delete(value)
        else:
            # node has no children
            if self.left is None and self.right is None:
                del self
                return None
            # node has one child
            elif self.left is None:
                temp = self.right
                del self
                return temp
            elif self.right is None:
                temp = self.left
                del self
                return temp
            # node has two children
            temp = self.get_min(self.right)
            self.value = temp.value
            self.right = self.right.delete(temp.value)
        return self

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        if self.left:
            self.left.in_order_print(self.left)

        print(self.value)

        if self.right:
            self.right.in_order_print(self.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        queue = []
        queue.append(node)

        while len(queue) > 0:
            current = queue.pop(0)
            print(current.value)

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        stack = []
        stack.append(node)

        while len(stack) > 0:
            current = stack.pop()
            print(current.value)

            if current.right:
                stack.append(current.right)

            if current.left:
                stack.append(current.left)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT

    def pre_order_dft(self, node):
        # visit the root
        print(node.value)
        # Traverse the left subtree
        if node.left:
            self.pre_order_dft(node.left)
        # Traverse the right subtree
        if node.right:
            self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        # Traverse the left subtree
        if node.left:
            self.post_order_dft(node.left)
        # Traverse the right subtree
        if node.right:
            self.post_order_dft(node.right)
        # visit the root
        print(node.value)
