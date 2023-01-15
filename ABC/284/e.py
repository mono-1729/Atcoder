import sys
from sys import stdin
sys.setrecursionlimit(3*10**5)
if "pypyjit" in sys.builtin_module_names:
	import pypyjit
	pypyjit.set_param("max_unroll_recursion=-1")
n,m=map(int,stdin.readline().split())
seen=[False]*n
# グラフ入力受取 (ここでは無向グラフを想定)
g=[[]for _ in range(n)]
for i in range(m):
	a,b=map(int,stdin.readline().split())
	g[a-1].append(b-1)
	g[b-1].append(a-1)
count=0
def dfs(v):
	global count
	count+=1
	if count==1000000:
		print(10**6)
		exit()
	seen[v] = True
	for next_v in g[v]: 
		if not seen[next_v]:
			dfs(next_v)
	seen[v] = False
dfs(0)
print(count)