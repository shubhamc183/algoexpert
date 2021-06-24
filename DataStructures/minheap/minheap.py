# https://www.youtube.com/watch?v=t0Cq6tVNRBA: Data Structures: Heaps
#	https://www.youtube.com/watch?v=g9YK6sftDi0: Implement A Binary Heap - An Efficient Implementation of The Priority Queue ADT (Abstract Data Type)

class MinHeap():

	def __init__(self):
		self._size, self._capacity, = 0, 10
		self._heap = [0] * self._capacity

	def _ensure_capacity(self):
		if self._size == self._capacity:
			self._heap.extend([0]*self._capacity)
			self._capacity *= 2

	def _swap(self, i, j):
		self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

	def _get_parent_index(self, idx):
		return (idx - 1) // 2

	def _get_left_child_index(self, idx):
		return idx * 2 + 1

	def _get_right_child_index(self, idx):
		return idx * 2 + 2

	def _hash_parent(self, idx):
		return self._get_parent_index(idx) >= 0

	def _has_left_child(self, idx):
		return self._get_left_child_index(idx) < self._size

	def _has_right_child(self, idx):
		return self._get_right_child_index(idx) < self._size

	def _parent(self, idx):
		return self._heap[self._get_parent_index(idx)]

	def _left_child(self, idx):
		return self._heap[self._get_left_child_index(idx)]

	def _right_child(self, idx):
		return self._heap[self._get_right_child_index(idx)]

	def peek(self):
		if self._size > 0:
			return self._heap[0]
		raise IndexError

	def add(self, number):
		self._ensure_capacity()
		self._heap[self._size] = number
		self._size += 1
		self._heapify_up()

	def remove(self):
		if self._size == 0:
			raise IndexError
		self._size -= 1
		self._heap[0] = self._heap[self._size]
		self._heapify_down()

	def _heapify_up(self):
		idx = self._size - 1
		# If parent exists and it's greater than current index
		while self._hash_parent(idx) and self._parent(idx) > self._heap[idx]:
			# swap the parent and current idx
			self._swap(self._get_parent_index(idx), idx)
			# make the parent as current idx
			idx = self._get_parent_index(idx)

	def _heapify_down(self):
		idx = 0
		# because if there is no left child then certainly there's no right child
		while self._has_left_child(idx):

			# get the smallest child index; it could be on left or right
			smaller_child_idx = self._get_left_child_index(idx)
			if self._has_right_child(idx) and self._right_child(idx) < self._left_child(idx):
				smaller_child_idx = self._get_right_child_index(idx)

			# if the child is smaller than the parent then make a swap!
			if self._heap[idx] > self._heap[smaller_child_idx]:
				self._swap(smaller_child_idx, idx)
				idx = smaller_child_idx
			else:
				break
