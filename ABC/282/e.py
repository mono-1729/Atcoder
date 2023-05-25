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
a=list(map(int,input().split()))
edges = []
ans=0
for i in range(n):
    for j in range(i+1,n):
        num=(pow(a[i],a[j],m)+pow(a[j],a[i],m))%m
        edges.append((-num,i,j))
uf = UnionFind(n)

# 重みが小さい順に辺をソート
edges.sort()

cost = 0

for edge in edges:
	c, u, v = edge
	# 頂点がつながっていなければ
	if not uf.same(u, v):
		cost += c # 重みを足し
		uf.union(u, v) # 頂点同士をつなげる
print(-cost)

