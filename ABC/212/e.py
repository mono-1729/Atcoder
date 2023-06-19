n,m,k=map(int,input().split())
edges=[[] for _ in range(n)]
for i in range(m):
    u,v=map(int,input().split())
    edges[u-1].append(v-1)
    edges[v-1].append(u-1)
dp=[0]*n
dp[0]=1
mod=998244353
for i in range(k):
	ndp=[0]*n
	dsum=sum(dp)
	for j in range(n):
		ndp[j]=dsum-dp[j]
		for k in edges[j]:
			ndp[j]-=dp[k]
		ndp[j]%=mod
	dp=ndp
print(dp[0])