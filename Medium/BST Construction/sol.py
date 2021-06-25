# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Average T.C: O(log n), S.C: O(1)
    # Worst T.C: O(n) if tree is one sided, S.C: O(1)
    def insert(self, value):
        current = self
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = BST(value)
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = BST(value)
                    break
                else:
                    current = current.right
        return self

    # Average T.C: O(log n), S.C: O(1)
    # Worst T.C: O(n) if tree is one sided, S.C: O(1)
    def contains(self, value):
        current = self
        while current:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def remove(self, value, parent_node=None):
        current = self
        while current:
            if value < current.value:
                parent_node = current
                current = current.left
            elif value > current.value:
                parent_node = current
                current = current.right
            else:
                if current.left and current.right:
                    # replace the current value with the smallest value from the right sub tree
                    current.value = current.right._get_min_value()
                    # remove the smallest node from the right sub tree
                    current.right.remove(current.value, current)
                elif parent_node is None:
                    # when it's the root node and it has only one child
                    if current.left:
                        current.value = current.left.value
                        current.right = current.left.right
                        current.left = current.left.left
                    elif current.right:
                        current.value = current.right.value
                        current.left = current.right.left
                        current.right = current.right.right
                elif parent_node.left == current:
                    parent_node.left = current.left if current.left is not None else current.right
                elif parent_node.right == current:
                    parent_node.right = current.left if current.left is not None else current.right
                break
        return self

    def _get_min_value(self):
        current = self
        while current.left:
            current = current.left
        return current.value
