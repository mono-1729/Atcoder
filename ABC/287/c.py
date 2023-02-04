from collections import defaultdict

class UnionFind():
	def __init__(self, n):
		self.n = n
		self.parents = [-1] * n

	def find(self, x):
		if self.parents[x] < 0:
			return x
		else:
			self.parents[x] = self.find(self.parents[x])
			return self.parents[x]

	def union(self, x, y):
		x = self.find(x)
		y = self.find(y)

		if x == y:
			return

		if self.parents[x] > self.parents[y]:
			x, y = y, x

		self.parents[x] += self.parents[y]
		self.parents[y] = x

	def size(self, x):
		return -self.parents[self.find(x)]

	def same(self, x, y):
		return self.find(x) == self.find(y)
n,m=map(int,input().split())
if m!=n-1:
	print('No')
	exit()
uni=UnionFind(n)
for i in range(m):
	u,v=map(int,input().split())
	uni.union(u-1,v-1)
if uni.size(0)==n:
	print('Yes')
else:
	print('No')
