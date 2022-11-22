n=int(input())
c=input().split()
g=[[]for _ in range(n)]
for i in range(n-1):
  a,b=map(int,input().split())
  g[a-1].append(b-1)
  g[b-1].append(a-1)
dp=[[0]*3 for i in range(100002)]
def dfs(pos,pre):
  v1,v2=1,1
  for i in g[pos]:
    if i==pre:
      continue
    dfs(i,pos)
    if c[pos]=='a':
      v1*=dp[i][0]+dp[i][2]
      v2*=dp[i][0]+dp[i][1]+2*dp[i][2]
    if c[pos]=='b':
      v1*=dp[i][1]+dp[i][2]
      v2*=dp[i][0]+dp[i][1]+2*dp[i][2]
    v1%=1000000007
    v2%=1000000007
  if c[pos]=='a':
    dp[pos][0]=v1
    dp[pos][2]=(v2-v1+1000000007)%1000000007
  if c[pos]=='b':
    dp[pos][1]=v1
    dp[pos][2]=(v2-v1+1000000007)%1000000007
    
dfs(0,-1)
print(dp[0][2])