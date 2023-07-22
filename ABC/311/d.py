from collections import deque
import sys
sys.setrecursionlimit(3*10**5)
if "pypyjit" in sys.builtin_module_names:
	import pypyjit
	pypyjit.set_param("max_unroll_recursion=-1")

n,m=map(int,input().split())
seen=[[False]*m for i in range(n)]
can=[[False]*m for i in range(n)]
s=[list(input()) for i in range(n)]

can[1][1]=True
seen[1][1]=True
dest=[(0,1),(1,0),(0,-1),(-1,0)]

def dfs(i,j,d):
	seen[i][j] = True
	x,y=dest[d]
	ni,nj=i,j
	while s[ni][nj]!='#':
		can[ni][nj]=True
		ni+=x
		nj+=y
	if not seen[ni-x][nj-y]:
		for k in range(4):
			dfs(ni-x,nj-y,k)

dfs(1,1,0)
dfs(1,1,1)
print(sum([sum(can[i]) for i in range(n)]))