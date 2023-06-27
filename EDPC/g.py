n,m=map(int,input().split())
edges=[[] for i in range(n)]
dims=[0 for i in range(n)]
for i in range(m):
    x,y=map(int,input().split())
    edges[x-1].append(y-1)
    dims[y-1]+=1
tsort=[]
dim0=[]
for i in range(n):
    if dims[i]==0:
        tsort.append(i)
        dim0.append(i)
while dim0:
    par=dim0.pop()
    for e in  edges[par]:
        dims[e]-=1
        if dims[e]==0:
            tsort.append(e)
            dim0.append(e)
num={}
for i in range(n):
    num[tsort[i]]=i
dp=[0]*(n)
for i in range(n):
    par=tsort[i]
    for e in edges[par]:
        dp[num[e]]=max(dp[num[e]],dp[i]+1)
print(max(dp))