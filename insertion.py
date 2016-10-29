from random import random as rnd
from time import time
import code

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

def evaluateAlgo(Algorithm=InsertionSort, inputSizes=[10,100,1000,10000]):
	times = []
	for inputSize in inputSizes:
		inSeq = [int(rnd()*1000) for i in range(inputSize)]	# randomly generate N(inputSize) numbers 0 bw 0 & 1000
		algo = Algorithm()
		outSeq, time = algo.sort(inSeq)
		times.append((inputSize, time))
	return times

if __name__ == '__main__':
	times = evaluateAlgo()
	print times