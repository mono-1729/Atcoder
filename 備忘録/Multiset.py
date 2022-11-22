from collections import defaultdict
import heapq
class LazyHeap():
	def __init__(self, init_arr=[]):
		self.heap = []
		self.lazy = defaultdict(int)
		self.len = 0
		for init_element in init_arr:
			heapq.heappush(self.heap, init_element)
			self.len += 1

	def __len__(self):
		return self.len

	def push(self, k):
		heapq.heappush(self.heap, k)
		self.len += 1

	def pop(self):
		self._clear()
		return heapq.heappop(self.heap)
		
	def get(self):
		self._clear()
		return self.heap[0]

	def _clear(self):
		while True:
			cand = self.heap[0]
			if cand in self.lazy and self.lazy[cand] > 0:
				heapq.heappop(self.heap)
				self.lazy[cand] -= 1

			else:
				return

	def remove(self, k):
		self.lazy[k] += 1
		self.len -= 1