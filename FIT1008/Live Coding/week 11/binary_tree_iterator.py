from linkedStack import linkedStack

class pre_order_binary_tree_iterator:
    def __init__(self,root_of_tree):
        self.root = root_of_tree
        self.remaining_stack = linkedStack()
        self.remaining_stack.push(self.root)

    def __iter__(self):
        return self

    def __next__(self):
        if self.remaining_stack.isEmpty():
            raise StopIteration
        current = self.remaining_stack.pop()
        if current.right:
            self.remaining_stack.push(current.right)
        if current.left:
            self.remaining_stack.push(current.left)
        return (current.key,current.value)