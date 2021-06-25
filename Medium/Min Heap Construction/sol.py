# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:

  # Solution is taken from https://www.youtube.com/watch?v=t0Cq6tVNRBA: Data Structures: Heaps

  def __init__(self, array):
    self.heap = self.buildHeap(array)

  # T.C: O(n)
  def buildHeap(self, array):
    self.size = 0
    self.heap = []
    for element in array:
      self.insert(element)
    return self.heap

  def _swap_heap_indicies(self, i, j): self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

  def _get_left_child_index(self, idx): return idx * 2 + 1

  def _get_right_child_index(self, idx): return idx * 2 + 2

  def _get_parent_index(self, idx): return (idx - 1) // 2

  def _has_left_child(self, idx): return self._get_left_child_index(idx) < self.size

  def _has_right_child(self, idx): return self._get_right_child_index(idx) < self.size

  def _has_parent(self, idx): return self._get_parent_index(idx) >= 0

  def _get_left_child(self, idx): return self.heap[self._get_left_child_index(idx)]

  def _get_right_child(self, idx): return self.heap[self._get_right_child_index(idx)]

  def _get_parent(self, idx): return self.heap[self._get_parent_index(idx)]

  # T.C: O(1) | S.C: O(1)
  def peek(self): return self.heap[0]

  # T.C: O(log n) | S.C: O(1)
  def insert(self, value):
    self.heap.append(value)
    self.size += 1
    self.siftUp()

  # T.C: O(log n) | S.C: O(1)
  def remove(self):
    top = self.heap[0]
    self.heap[0] = self.heap.pop()
    self.size -= 1
    self.siftDown()
    return top

  # T.C: O(log n) | S.C: O(1)
  def siftUp(self):
    idx = self.size - 1
    # If the index has parent and the parent is greater than the index
    while self._has_parent(idx) and self._get_parent(idx) > self.heap[idx]:
      # swap there values
      self._swap_heap_indicies(self._get_parent_index(idx), idx)
      # make parent the index to further check it's parent....
      idx = self._get_parent_index(idx)

  # T.C: O(log n) | S.C: O(1)
  def siftDown(self):
    idx = 0
    # checking left side gaurentees if the idx has child(ren)
    while self._has_left_child(idx):
      smaller_child_idx = self._get_left_child_index(idx)

      # now check if right child exist and if it's even smaller
      if self._has_right_child(idx) and self._get_right_child(idx) < self.heap[smaller_child_idx]:
        smaller_child_idx = self._get_right_child_index(idx)

      # check if any children of idx is smaller than it else break
      if self.heap[idx] > self.heap[smaller_child_idx]:
        self._swap_heap_indicies(idx, smaller_child_idx)
        idx = smaller_child_idx
      else:
        break