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
    
    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members
n,m=map(int,input().split())
uv=[[] for i in range(n+1)]
uni=UnionFind(n)
for i in range(m):
    u,v=map(int,input().split())
    uv[u-1].append(v-1)
    uv[v-1].append(u-1)
    uni.union(u-1,v-1)
mem=uni.all_group_members()
nn=[0]*n
for i in range(n):
    nn[uni.find(i)]+=len(uv[i])
for i in range(n):
	if not len(mem[i])*2==nn[i]:
		print('No')
		exit()
print('Yes')
    