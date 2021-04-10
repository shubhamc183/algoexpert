# Time Complexity: Avg: O(logN) as we are halfing the tree everytime
# Time Complexity: Avg: O(N) if it's single branch BST and value is at the leaf
# Space Complexity: O(logN) as are addding O(logN) call stacks
def findClosestValueInBst1(tree, target):
	if tree.value == target:
		return target
	_child = 10**10
	if tree.value < target and tree.right is not None:
		_child = findClosestValueInBst(tree.right, target)
	elif tree.value > target and tree.left is not None:
		_child = findClosestValueInBst(tree.left, target)
	return tree.value if abs(target - tree.value ) < abs(target- _child) else _child

def findClosestValueInBst2(tree, target):
	return findClosestValueInBstHelper(tree, target, tree.value)

# Time Complexity: is same as upper solution
# Space Complexity: O(1) as are keeping just contant space, i.e one variable
# For interative solution is here more optimal
def findClosestValueInBstHelper(tree, target, closest):
	current_node = tree
	while current_node is not None:
		if abs(target - closest) > abs(target - current_node.value):
			closest = current_node.value
		if target < current_node.value:
			current_node = current_node.left
		elif target > current_node.value:
			current_node = current_node.right
		else:
			break
	return closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
