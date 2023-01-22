n,x=map(int,input().split())
ab=[list(map(int,input().split())) for i in range(n)]
dp=[[0]*(x+1)for i in range(n+1)]
dp[0][0]=1
for i in range(n):
    for j in range(x+1):
        for k in range(ab[i][1]+1):
            if j+k*ab[i][0]<=x:
            	dp[i+1][j+k*ab[i][0]]=max(dp[i][j],dp[i+1][j+k*ab[i][0]])
if dp[n][x]==1:
    print('Yes')
else:
    print('No')