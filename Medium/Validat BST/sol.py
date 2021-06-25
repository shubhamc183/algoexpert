# This is an input class. Do not edit.
class BST:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

# T.C: O(n): number of nodes
# S.C: O(d): depth(height) of the tree; recursion call stack
def validateBst(tree, _min=float('-inf'), _max=float('inf')):
  if tree is None:
	  return True
	if tree.value < _min or tree.value >= _max:
		return False
	return validateBst(tree.left, _min, tree.value) and validateBst(tree.right, tree.value, _max)