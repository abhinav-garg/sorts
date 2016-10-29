from random import random as rnd
from time import time
import code
import matplotlib.pyplot as plt

plt.ion()
fig, ax = plt.subplots()
ax.set_xlabel('Input Size')
ax.set_ylabel('Time')

ax.set_xscale('log')
ax.set_yscale('log')

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

class EvaluateAlgo:
	def __init__(self, inputSizes=[10,100,1000], average=3):
		self.inputSizes = inputSizes
		self.average = average

	def setParams(self, inputSizes=[10,100,1000], average=3):
		self.inputSizes = inputSizes # Input sizes for which algo is run
		self.average = average # Averaging over 3 runs for same size

	def evaluate(self, Algorithm=InsertionSort):
		self.algo = Algorithm()
		self.times = []
		for inputSize in self.inputSizes:
			totalTime = 0
			for i in range(self.average):
				# randomly generate N(inputSize) numbers 0 bw 0 & 1000
				inSeq = [int(rnd()*1000) for i in range(inputSize)]	
				outSeq, time = self.algo.sort(inSeq)
				totalTime += time
			avgTime = totalTime/self.average
			self.times.append((inputSize, avgTime))
		return self.times

	def plot(self, ax):
		xVals, yVals = [list(t) for t in zip(*self.times)]
		ax.plot(xVals, yVals, '-o',label=self.algo.__class__.__name__)
		plt.legend()
		plt.draw()

if __name__ == '__main__':
	evaluate = EvaluateAlgo(inputSizes=[10,100,1000,10000], average=1)
	times = evaluate.evaluate()
	evaluate.plot(ax)
	print times
	code.interact(local=dict(globals(), **locals()))