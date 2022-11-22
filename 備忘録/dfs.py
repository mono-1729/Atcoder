from collections import deque

n=int(input())
seen=[False]*n
check=[False]*n

first_order=[0]*n
last_order=[0]*n

n,m=map(int,input().split())

# グラフ入力受取 (ここでは無向グラフを想定)
g=[[]for i in range(n)]
for i in range(n):
	a,b=map(int,input().split())
	g[a].append(b)
	g[b].append(a)
def dfs(G, v):
	seen[v] = True
	for next_v in G[v]: 
		if seen[next_v]:
			print(-1)
			exit()
		dfs(G, next_v)
	seen[v] = False

#経路保存


import sys
sys.setrecursionlimit(5000)
flag=0
ans=[[]for i in range(10007)]
c=[0 for i in range(10007)]
l=[]
n,q=map(int,input().split())
a=list(map(int,input().split()))
xy=[[]for i in range(n+1)]
for i in range(q):
	x,y=map(int,input().split())
	xy[x].append(y)
def dfs(pos, dep):
	global flag
	#global l
	#print(l)
	#global ans
	#global n
	if flag:
		return
	if pos == n+1:
		ans[dep].append(l.copy())
		#print(dep)
		#print(l)
		if  len(ans[dep])==2:
			flag=1
		return
	dfs(pos+1,dep)
	if c[pos]==0:
		l.append(pos)
		for i in xy[pos]:
			c[i]+=1
		dfs(pos+1,dep+a[pos-1])
		for i in xy[pos]:
			c[i]-=1
		l.pop()
dfs(1,0)
for i in range(1,10000):
	if len(ans[i])<=1:
		continue
	print(len(ans[i][0]))
	e8=list(map(str,ans[i][0]))
	print(' '.join(e8))
	print(len(ans[i][1]))
	sq=list(map(str,ans[i][1]))
	print(' '.join(sq))
	"""
	print(len(ans[i]))
	print(i)
	print(xy)
	print(ans[:10]) 
	"""
	exit()

