# T.C: O(n)
# S.C: O(n)
def invertBinaryTreeRecusrsion(tree):
  if tree is None:
    return
  invertBinaryTree(tree.left)
  invertBinaryTree(tree.right)
	tree.right, tree.left = tree.left, tree.right

def invertBinaryTreeQueueDFS(tree):
	queue = [tree]
	while queue:
		current = queue.pop()
		if current is None:
			continue
		current.right, current.left = current.left, current.right
		queue.append(current.left)
		queue.append(current.right)


# This is the class of the input binary tree.
class BinaryTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None