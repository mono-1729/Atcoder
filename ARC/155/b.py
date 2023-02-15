from bisect import bisect_right,bisect_left
#(フェニック木)
class BIT:
	# 長さN+1の配列を初期化
	def __init__(self, N):
		self.size = N
		self.bit = [0]*(N+1)

	# i番目までの和を求める
	def sum(self, i):
		res = 0
		while i > 0:
			res += self.bit[i] # フェニック木のi番目の値を加算
			i -= -i & i # 最も右にある1の桁を0にする
		return res

	# i番目の値にxを足して更新する
	def add(self, i, x):
		while i <= self.size:
			self.bit[i] += x # フェニック木のi番目にxを足して更新
			i += -i & i # 最も右にある1の桁に1を足す
q,a,b=map(int,input().split())
tab=[]
num=[(a-b,0),(a+b,1)]
for i in range(q):
	t,a,b=map(int,input().split())
	tab.append((t,a,b))
	if t==1:
		num.append(a-b,(i+1)*2)
		num.append(a+b,(i+1)*2+1)
num.sort()
for i in range(len(num)):
	x,y=num[i]
	num[i]=(y,i+1,x)
num.sort()
bit=BIT(len(num))
bit.add(num[0][1],1)
bit.add(num[1][1],1)
count=2
for i in range(q):
	t,aa,bb=tab[i]
	if t==1:
		bit.add(num[count][1],1)
		bit.add(num[count+1][1],1)
	if t==2:
		left=bisect_left(num,aa)
		right=bisect_right(num,bb)
		if left==right:
			ans=10**10
			if left!=0:
				ans=aa-num[left-1]
			if right!=len(num):
				ans=min(ans,num[right]-bb)
			print(ans)
		else:
			print(0)
