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
while True:
	w,h=map(int,input().split())
	if w==h==0 :
		exit()
	field=[[-1]*w for _ in range(h)]
	land=[]
	num=0
	for i in range(h):
		clist=list(map(int,input().split()))
		for j,c in enumerate(clist):
			if c==1:
				field[i][j]=num
				num+=1
				land.append([i,j])
	if num==0:
		print(0)
		continue
	sample=UnionFind(num)
	for i,j in land: 
		k=field[i][j]
		if i!=0:
			if j!=0:
				if field[i-1][j-1]!=-1:
					sample.union(field[i-1][j-1],k)
			if j!=w-1:
				if field[i-1][j+1]!=-1:
					sample.union(field[i-1][j+1],k)
			if field[i-1][j]!=-1:
				sample.union(field[i-1][j],k)
		if i!=h-1:
			if j!=0:
				if field[i+1][j-1]!=-1:
					sample.union(field[i+1][j-1],k)
			if j!=w-1:
				if field[i+1][j+1]!=-1:
					sample.union(field[i+1][j+1],k)
			if field[i+1][j]!=-1:
				sample.union(field[i+1][j],k)
		if j!=0:
			if field[i][j-1]!=-1:
				sample.union(field[i][j-1],k)
		if j!=w-1:
			if field[i][j+1]!=-1:
				sample.union(field[i][j+1],k)
	print(sample.group_count())