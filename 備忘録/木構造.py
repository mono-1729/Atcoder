import sys
sys.setrecursionlimit(100000)
n=int(input())
tree=[[] for i in range(n)]
dp=[0 for i in range(n)]
ab=[]
for i in range(n-1):
  a,b=map(int,input().split())
  tree[a-1].append(b-1)
  tree[b-1].append(a-1)
  ab.append([a-1,b-1])

def dfs(pos,pre):
  dp[pos]=1
  for i in tree[pos]:
    if i!=pre:
      dfs(i,pos)
      dp[pos]+=dp[i]
dfs(0,-1)
ans=0
for i in range(n-1):
  r=min(dp[ab[i][0]],dp[ab[i][1]])
  ans+=r*(n-r)
print(ans)