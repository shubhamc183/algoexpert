# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    return binary_tree_diameter_util(tree)[1]

# T.C: O(n); n is the number of nodes in the tree
# S.C: O(h); h is the hieght of tree
def binary_tree_diameter_util(tree):
    if tree is None:
        return 0, 0
    left_hieght, left_diameter = binary_tree_diameter_util(tree.left)
    right_hieght, right_diameter = binary_tree_diameter_util(tree.right)
    return 1 + max(left_hieght, right_hieght), max(left_hieght + right_hieght, left_diameter, right_diameter)
