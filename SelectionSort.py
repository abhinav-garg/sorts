from time import time
import code

class SelectionSort:
	def __init__(self, inSeq = []):
		self.inSeq = inSeq
		self.time = -1
		self.outSeq = []

	def sort(self, inSeq):
		self.inSeq = list(inSeq)
		self.outSeq = list(inSeq)
		t0 = time()

		for i in range(len(self.outSeq)-1):
			j = i+1
			small = self.outSeq[j]
			smallInd = j
			while j < len(self.outSeq)-1:
				j += 1
				if self.outSeq[j] < small:
					small = self.outSeq[j]
					smallInd = j
			if self.outSeq[i] >  self.outSeq[smallInd]:
				self.outSeq[i], self.outSeq[smallInd] = self.outSeq[smallInd], self.outSeq[i]
			# code.interact(local=dict(globals(), **locals()))
		t1 = time()
		self.time = t1-t0
		return self.outSeq, self.time

# # Debug
# a = [5,4,3,2,1]
# s = SelctionSort()
# b = s.sort(a)
# code.interact(local=dict(globals(), **locals()))