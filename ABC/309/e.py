from collections import defaultdict
from collections import deque
import sys
sys.setrecursionlimit(4*10**5)
n,m=map(int,input().split())
edge=[[]for i in range(n)]
p=list(map(int,input().split()))
for i in range(n-1):
    edge[i+1].append(p[i]-1)
    edge[p[i]-1].append(i+1)
h=defaultdict(int)
for i in range(m):
    x,y=map(int,input().split())
    h[x-1]=max(h[x-1],y+1)
seen=[False]*n
ans=[0]*n
def dfs(v,num):
	num=max(num,h[v])
	if num>0:
		ans[v]=1
	seen[v] = True
	for next_v in edge[v]: 
		if seen[next_v]:
			continue
		dfs(next_v,num-1)
dfs(0,0)
print(sum(ans))