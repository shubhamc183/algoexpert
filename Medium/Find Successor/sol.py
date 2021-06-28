# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

# T.C: O(n), n is the number of nodes in the tree
# S.C: O(h), h is the height of the tree
def findSuccessor1(tree, node):
    successor = {'successor': False}
    return find_successor_util(tree, node, successor)

def find_successor_util(tree, node, successor):
	if tree is None:
        return None
    _ = find_successor_util(tree.left, node, successor)
    if _:
        return _
    if successor['successor'] == True:
        return tree
    if tree.value == node.value:
        successor['successor'] = True
    _ = find_successor_util(tree.right, node, successor)
    if _:
        return _

# T.C: O(h)
# S.C: O(1)
def findSuccessor(tree, node):
    if node.right:
        return find_left_most_child(node.right)
    return find_right_most_parent(node)

def find_left_most_child(node):
    current = node
    while current and current.left:
        current = current.left
    return current

def find_right_most_parent(node):
    current = node
    while current.parent and current.parent.right == current:
        current = current.parent
    return current.parent