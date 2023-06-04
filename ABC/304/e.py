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

	def members(self, x):
		root = self.find(x)
		return [i for i in range(self.n) if self.find(i) == root]

	def roots(self):
		return [i for i, x in enumerate(self.parents) if x < 0]

	def group_count(self):
		return len(self.roots())

	def all_group_members(self):
		group_members = defaultdict(list)
		for member in range(self.n):
			group_members[self.find(member)].append(member)
		return group_members

	def __str__(self):
		return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())
n,m=map(int,input().split())
uf=UnionFind(n)
uv=[list(map(int,input().split())) for i in range(m)]
for i in range(m):
	uf.union(uv[i][0]-1,uv[i][1]-1)
k=int(input())
xy=[list(map(int,input().split())) for i in range(k)]
no=set()
for i in range(k):
	x,y=xy[i]
	xx=uf.find(x-1)
	yy=uf.find(y-1)
	no.add((min(xx,yy),max(xx,yy)))
Q=int(input())
for i in range(Q):
	p,q=map(int,input().split())
	pp=uf.find(p-1)
	qq=uf.find(q-1)
	if (min(pp,qq),max(pp,qq)) in no:
		print('No')
	else:
		print('Yes')