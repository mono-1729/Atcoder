import sys
sys.setrecursionlimit(3*10**5)
n,k=map(int,input().split())
g=[[] for i in range(n)]
for i in range(n-1):
    a,b=map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)
def dfs(cu,pa,rest):
	res=rest%(10**9+7)
	used=1
	if cu:
		used+=1
	for to in g[cu]:
		if to!=pa:
			res*=dfs(to,cu,k-used)
			res%=(10**9+7)
			used+=1
	return res
print(dfs(0,-1,k))