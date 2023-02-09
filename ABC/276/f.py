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
n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(n):
	a[i]=(a[i],i)
a.sort()
for i in range(n):
	x,y=a[i]
	a[i]=(y,i,x)
a.sort()
bit=BIT(n)
bb=BIT(n)
cumul=0
num=0
for i in range(n):
	_,order,aa=a[i]
	cumul+=aa
	num+=(cumul-bit.sum(order+1))*2
	num+=aa*(2*bb.sum(order+1)-1)
	b.append(aa)
	bit.add(order+1,aa)
	bb.add(order+1,1)
	num%=998244353
	print((num*pow((i+1)**2,998244351,998244353))%998244353)
