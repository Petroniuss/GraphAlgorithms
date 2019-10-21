def low_priority(a, b):
	return a < b

def high_priority(a, b):
	return a > b

class Priority_Queue:
	
	def __init__(self, max_len, cmp = high_priority):
		self.arr = [-1 for i in range(max_len)]
		self.pos = [-1 for i in range(max_len)]
		self.max_len = max_len
		self.cmp = cmp
		self.length = 0

	def push(self, value, v):
		self.arr[self.length] = value
		self.pos[v] = self.length
		self.length = self.length + 1

	def contains(self, v):
		return v < self.length and self.pos[v] != -1

	def parent(self, i):
		return (i - 1) // 2

	def left(self, i):
		return (i * 2) + 1

	def right(self, i):
		return (i * 2) + 2

	def swap(self, arr, a, b):
		arr[a], arr[b] = arr[b], arr[a]

