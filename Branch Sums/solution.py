# https://www.algoexpert.io/questions/Branch%20Sums

# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
	branch_sum_array = []
	calculate_sub_sum(root, 0, branch_sum_array)
	return branch_sum_array


def calculate_sub_sum(root, sum_till_here, branch_sum_array):
	if root is None:
		return
	sum_till_here += root.value
	if root.left is None and root.right is None:
		branch_sum_array.append(sum_till_here)
		return
	calculate_sub_sum(root.left, sum_till_here, branch_sum_array)
	calculate_sub_sum(root.right, sum_till_here, branch_sum_array)
