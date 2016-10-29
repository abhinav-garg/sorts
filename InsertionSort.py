from time import time

class InsertionSort:
	def __init__(self, inSeq = []):
		self.inSeq = inSeq
		self.time = -1
		self.outSeq = []

	def sort(self, inSeq):
		self.inSeq = list(inSeq)
		self.outSeq = list(inSeq)
		t0 = time()
		for j in range(1, len(self.outSeq)):
			key = self.outSeq[j]
			i = j-1
			while i >= 0 and self.outSeq[i] > key:
				self.outSeq[i+1] = self.outSeq[i]
				i -= 1
			self.outSeq[i+1] = key
		t1 = time()
		self.time = t1-t0
		return self.outSeq, self.time