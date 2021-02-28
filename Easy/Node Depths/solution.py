# https://www.algoexpert.io/questions/Node%20Depths

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# O(n) time complexity
# O(h) space complexity where h is the height of tree; stack call


def nodeDepths(root, depth_till_here=0):
    if root is None:
        return 0
    return depth_till_here + nodeDepths(root.left, depth_till_here + 1) + nodeDepths(root.right, depth_till_here + 1)
