#####segfunc#####
def segfunc(x, y):
	return max(x,y)
#################

#####ide_ele#####
ide_ele =0
#################

class SegTree:
	"""
	init(init_val, ide_ele): 配列init_valで初期化 O(N)
	update(k, x): k番目の値をxに更新 O(logN)
	query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
	"""
	def __init__(self, init_val, segfunc, ide_ele):
		"""
		init_val: 配列の初期値
		segfunc: 区間にしたい操作
		ide_ele: 単位元
		n: 要素数
		num: n以上の最小の2のべき乗
		tree: セグメント木(1-index)
		"""
		n = len(init_val)
		self.segfunc = segfunc
		self.ide_ele = ide_ele
		self.num = 1 << (n - 1).bit_length()
		self.tree = [ide_ele] * 2 * self.num
		# 配列の値を葉にセット
		for i in range(n):
			self.tree[self.num + i] = init_val[i]
		# 構築していく
		for i in range(self.num - 1, 0, -1):
			self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

	def update(self, k, x):
		"""
		k番目の値をxに更新
		k: index(0-index)
		x: update value
		"""
		k += self.num
		self.tree[k] = max(self.tree[k],x)
		while k > 1:
			self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
			k >>= 1


	def add(self, k, x):
		"""
		k番目の値にx加算
		k: index(0-index)
		x: update value
		"""
		k += self.num
		self.tree[k] += x
		while k > 1:
			self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
			k >>= 1


	def query(self, l, r):
		"""
		[l, r)のsegfuncしたものを得る
		l: index(0-index)
		r: index(0-index)
		"""
		res = self.ide_ele

		l += self.num
		r += self.num
		while l < r:
			if l & 1:
				res = self.segfunc(res, self.tree[l])
				l += 1
			if r & 1:
				res = self.segfunc(res, self.tree[r - 1])
			l >>= 1
			r >>= 1
		return res
n=int(input())
hwd=[]
h=set()
w=set()
d=set()
for i in range(n):
	l=list(map(int,input().split()))
	l.sort(reverse=True)
	hwd.append(l)
	h.add(l[0])
	w.add(l[1])
	d.add(l[2])
h=list(h)
h.sort()
w=list(w)
w.sort()
d=list(d)
d.sort()
hd=dict()
wd=dict()
dd=dict()
for i in range(len(h)):
	hd[h[i]]=i+1
for i in range(len(w)):
	wd[w[i]]=i+1
for i in range(len(d)):
	dd[d[i]]=i+1
for i in range(n):
	p,q,r=hwd[i]
	hwd[i]=(hd[p],wd[q],dd[r])
hwd.sort(reverse=True)
seg=SegTree([0]*(n+1),segfunc,0)
count=0
#print(hwd)
for i in reversed(range(1,len(h)+1)):
	wait=[]
	while count<n and hwd[count][0]==i:
		z,x,y=hwd[count]
		if seg.query(x,n+1)>y:
			print('Yes')
			exit()
		wait.append((x,y))
		count+=1
	for w in wait:
		seg.update(w[0]-1,w[1])
print('No')