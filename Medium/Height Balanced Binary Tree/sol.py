# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def calculate_height(tree):
    if tree is None:
        return 0
    return 1 + max(calculate_height(tree.left), calculate_height(tree.right))

def heightBalancedBinaryTree1(tree):
    if tree is None:
        return True
    return heightBalancedBinaryTree(tree.left) and \
            heightBalancedBinaryTree(tree.right) and \
                abs(calculate_height(tree.left) - calculate_height(tree.right)) <= 1

# T.C: O(n); n is the number of the node; as we are touching each element once
# S.C: O(h); h is the hieght of the tree; recursion call stack
def heightBalancedBinaryTree(tree):
    return hbbt_util(tree)[0]

def hbbt_util(tree):
    if tree is None:
        return True, -1
    # CHECK if left subtree is balanced and get the height too so that we don't need to calulate again
    left_subtree_balanced, left_subtree_hieght = hbbt_util(tree.left)
    if not left_subtree_balanced:
        return False, -1
    right_subtree_balanced, right_subtree_hieght = hbbt_util(tree.right)
    # CHECK if right subtree is balanced and get the height too so that we don't need to calulate again
    if not right_subtree_balanced:
        return False, -1
    if abs(left_subtree_hieght - right_subtree_hieght) <= 1:
        return True, 1 + max(left_subtree_hieght, right_subtree_hieght)
    return False, -1
