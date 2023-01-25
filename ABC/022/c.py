from collections import deque
import sys
sys.setrecursionlimit(3*10**5)
if "pypyjit" in sys.builtin_module_names:
	import pypyjit
	pypyjit.set_param("max_unroll_recursion=-1")
n,m=map(int,input().split())
# グラフ入力受取 (ここでは無向グラフを想定)
g=[[]for i in range(n)]
for i in range(m):
	u,v,l=map(int,input().split())
	g[u-1].append((v-1,l))
	g[v-1].append((u-1,l))
 
def bfs(s):
	dist = [10**9]*n
	que = deque([s])
	dist[s] = 0
	flg=True
	while que:
		v = que.popleft()
		d = dist[v]
		for w0,w1 in g[v]:
			if flg and w0==0:
				flg=False
				continue  
			dd=d+w1
			if dist[w0]<=dd:
				continue
			dist[w0]=dd
			que.append(w0)
	return dist[0]
ans=10**9
for x0,x1 in g[0]:
	num=x1+bfs(x0)
	ans=min(ans,num)
if ans==10**9:
	print(-1)
else:
	print(ans)