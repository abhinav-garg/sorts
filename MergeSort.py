from time import time
import code

INF = float('inf')

class MergeSort:
	def __init__(self, inSeq = []):
		self.inSeq = inSeq
		
	def sort(self, inSeq, p=0, r=INF):
		self.inSeq = inSeq
		if r == INF: r = len(inSeq)-1
		if p < r:
			q = (p+r)/2
			self.sort(inSeq, p, q)
			self.sort(inSeq, q+1, r)
			self.merge(inSeq,p,q,r)
		
		return self.inSeq

	def merge(self, inSeq, p, q, r):
		A = inSeq
		n1 = q - (p-1)
		n2 = r - q
		L = [0]*(n1+1)
		R = [0]*(n2+1)
		for i in range(n1):
			L[i] = A[p+i]
		for j in range(n2):
			R[j] = A[q+j+1]
		L[n1] = INF
		R[n2] = INF
		i = 0
		j = 0
		for k in range(p,r+1):
			if L[i] <= R[j]:
				A[k] = L[i]
				i += 1
			else:
				A[k] = R[j]
				j += 1
		# if q == 0:
		# 	code.interact(local=dict(globals(), **locals()))

# # Debug
# a = [5,4,3,2,1,6]
# s = MergeSort()
# t0 = time()
# b = s.sort(a)
# t1 = time()
# time = t1-t0
# code.interact(local=dict(globals(), **locals()))