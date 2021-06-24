import unittest
from minheap import MinHeap

class TestMinHeap(unittest.TestCase):
	min_heap = MinHeap()

	def test_a_empty_heap(self):
		with self.assertRaises(IndexError):
			self.min_heap.peek()

	def test_b_add(self):
		self.min_heap.add(10)
		self.min_heap.add(4)
		self.min_heap.add(15)
		self.assertEqual(4, self.min_heap.peek())
		self.assertListEqual([4, 10, 15, 0, 0, 0, 0, 0, 0, 0], self.min_heap._heap)

	def test_c_remove(self):
		self.min_heap.remove()
		self.assertListEqual([10, 15, 15, 0, 0, 0, 0, 0, 0, 0], self.min_heap._heap)

	def test_d_add_remove(self):
		self.min_heap.add(20)
		self.min_heap.add(0)
		self.min_heap.add(30)
		self.assertListEqual([0, 10, 20, 15, 30, 0, 0, 0, 0, 0], self.min_heap._heap)
		self.min_heap.remove()
		self.min_heap.remove()
		self.min_heap.add(2)
		self.min_heap.add(4)
		self.min_heap.add(1)
		self.min_heap.add(-3)
		self.assertEqual(-3, self.min_heap.peek())
		self.assertListEqual([-3, 4, 1, 30, 15, 20, 2, 0, 0, 0], self.min_heap._heap)


if __name__ == '__main__':
    unittest.main()