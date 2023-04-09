from collections import deque
import sys
sys.setrecursionlimit(3*10**5)
if "pypyjit" in sys.builtin_module_names:
	import pypyjit
	pypyjit.set_param("max_unroll_recursion=-1")
n=int(input())
a=list(map(int,input().split()))
seen=[False]*n
check=[False]*n
h=[0]*n
n,m=map(int,input().split())

g=[[]for i in range(n)]
for i in range(n):
	g[i].append(a[i]-1)
def dfs(G, v):
	seen[v] = True
	if seen[G[v]]:
		dfs2(G,G[v])
	else:
		dfs(G, G[v])
	seen[v] = False
def dfs2(G, v):
	seen[v] = True
	if seen[G[v]]:
		dfs2(G,G[v])
	else:
		dfs(G, G[v])
	seen[v] = False
for i in range(n):
	if not check[i]:
		dfs(g,i)

