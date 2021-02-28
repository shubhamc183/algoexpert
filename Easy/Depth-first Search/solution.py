# https://www.algoexpert.io/questions/Depth-first%20Search

# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
  def __init__(self, name):
      self.children = []
      self.name = name

  def addChild(self, name):
      self.children.append(Node(name))
      return self

# V is number of Vertices or Node
# E is number of Edges
# Time: O(V + E)
# Space: O(V)
  def depthFirstSearch(self, array):
  array.append(self.name)
  for child in self.children:
    child.depthFirstSearch(array)
  return array
