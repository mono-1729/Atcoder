from functools import lru_cache
import sys
sys.setrecursionlimit(8*10**5)
n=int(input())
g=[[] for i in range(n)]
ans=[]
for i in range(n-1):
	a,b=map(int,input().split())
	g[a-1].append(b-1)
	g[b-1].append(a-1)
def main(i,pre):
	for j in g[i]:
		if j!=pre:
			ans.append(len(g[j]))
			for k in g[j]:
				if k!=i and len(g[k])==2:
					for x in g[k]:
						if x!=j:
							main(x,k)
for i in range(n):
	if len(g[i])==1:
		main(i,-1)
		break
ans.sort()
print(*ans)