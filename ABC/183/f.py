class UnionFind():
	def __init__(self, n,c):
		self.n = n
		self.parents = [{c[i]:1} for i in range(n)]
	def find(self, x):
		if type(self.parents[x]) is dict:
			return x
		else:
			self.parents[x] = self.find(self.parents[x])
			return self.parents[x]

	def union(self, x, y):
		x = self.find(x)
		y = self.find(y)

		if x == y:
			return

		if len(self.parents[x]) < len(self.parents[y]):
			x, y = y, x

		for k,v in self.parents[y].items():
			if k in self.parents[x].keys():
				self.parents[x][k]+=v
			else:
				self.parents[x][k]=v
		self.parents[y] = x

	def size(self, x,num):
		return self.parents[self.find(x)][num] if num in self.parents[self.find(x)] else 0

n,q=map(int,input().split())
c=list(map(int,input().split()))
uni=UnionFind(n,c)
for i in range(q):
	k,a,b=map(int,input().split())
	if k==1:
		uni.union(a-1,b-1)
	else:
		print(uni.size(a-1,b))
