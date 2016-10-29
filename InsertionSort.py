from time import time
import code

class InsertionSort:
	def __init__(self, inSeq = []):
		self.inSeq = inSeq
		
	def sort(self, inSeq):
		self.inSeq = inSeq
		for j in range(1, len(self.inSeq)):
			key = self.inSeq[j]
			i = j-1
			while i >= 0 and self.inSeq[i] > key:
				self.inSeq[i+1] = self.inSeq[i]
				i -= 1
			self.inSeq[i+1] = key
		return self.inSeq

# # Debug
# a = [5,4,3,2,1]
# s = InsertionSort()
# t0 = time()
# b = s.sort(a)
# t1 = time()
# time = t1-t0
# code.interact(local=dict(globals(), **locals()))