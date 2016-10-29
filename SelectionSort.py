from time import time
import code

class SelectionSort:
	def __init__(self, inSeq = []):
		self.inSeq = inSeq
		
	def sort(self, inSeq):
		self.inSeq = inSeq
		for i in range(len(self.inSeq)-1):
			j = i+1
			small = self.inSeq[j]
			smallInd = j
			while j < len(self.inSeq)-1:
				j += 1
				if self.inSeq[j] < small:
					small = self.inSeq[j]
					smallInd = j
			if self.inSeq[i] >  self.inSeq[smallInd]:
				self.inSeq[i], self.inSeq[smallInd] = self.inSeq[smallInd], self.inSeq[i]
		return self.inSeq

# # Debug
# a = [5,4,3,2,1]
# s = SelectionSort()
# t0 = time()
# b = s.sort(a)
# t1 = time()
# time = t1-t0
# code.interact(local=dict(globals(), **locals()))