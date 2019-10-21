#GeeksForGeeks implementation of min heap. 
# Of course it had a bug...
from heapq import heappush, heappop, heapify, _heappop_max, _heapify_max

# heappop - pop and return the smallest element from heap 
# heappush - push the value item onto the heap, maintaining 
#			 heap invarient 
# heapify - transform list into heap, in place, in linear time 

# A class for Min Heap 
class MaxHeap: 
	def __init__(self): 
		self.heap = []
		self.pos = []

	def parent(self, i): 
		return (i-1) // 2
	
	# Inserts a new key 'k' 
	def insertKey(self, k): 
		heappush(self.heap, -k)		 

	# Decrease value of key at index 'i' to new_val 
	# It is assumed that new_val is smaller than heap[i] 
	def increase_key(self, i, new_val): 
		self.heap[i] = (-1) * new_val 
		while(i != 0 and self.heap[self.parent(i)] > self.heap[i]): 
			# Swap heap[i] with heap[parent(i)] 
			self.heap[i] , self.heap[self.parent(i)] = ( 
			self.heap[self.parent(i)], self.heap[i]) 

			i = self.parent(i)
			
	# Method to remove minium element from min heap 
	def extractMax(self): 
		return - heappop(self.heap)  

	# Get the minimum element from the heap 
	def getMax(self): 
		return - self.heap[0] 

	def show(self):
		for v in self.heap:
			print(v, end='|')

# A class for Min Heap 
class MinHeap: 
	
	# Constructor to initialize a heap 
	def __init__(self): 
		self.heap = [] 

	def parent(self, i): 
		return (i-1)//2
	
	# Inserts a new key 'k' 
	def insertKey(self, k): 
		heappush(self.heap, k)		 

	# Decrease value of key at index 'i' to new_val 
	# It is assumed that new_val is smaller than heap[i] 
	def decreaseKey(self, i, new_val): 
		self.heap[i] = new_val 
		while(i != 0 and self.heap[self.parent(i)] > self.heap[i]): 
			# Swap heap[i] with heap[parent(i)] 
			self.heap[i] , self.heap[self.parent(i)] = ( 
			self.heap[self.parent(i)], self.heap[i]) 
			
	# Method to remove minium element from min heap 
	def extractMin(self): 
		return heappop(self.heap) 

	# This functon deletes key at index i. It first reduces 
	# value to minus infinite and then calls extractMin() 
	def deleteKey(self, i): 
		self.decreaseKey(i, float("-inf")) 
		self.extractMin() 

	# Get the minimum element from the heap 
	def getMin(self): 
		return self.heap[0] 