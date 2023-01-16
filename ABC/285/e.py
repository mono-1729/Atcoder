n=int(input())
a=list(map(int,input().split()))
dp=[[0]*n for i in range(n)]
b=[0]*n
for i in range(n-1):
	b[i+1]=b[i]+a[i//2]
for i in range(n-1):
	for j in range(i+1):
		dp[i+1][j+1]=dp[i][j]
		dp[i+1][0]=max(dp[i+1][0],dp[i][j]+b[j])
ans=0
for i in range(n):
	ans=max(ans,dp[n-1][i]+b[i])
print(ans)