n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
dp=[[10*9]*(m+1)for i in range(n+1)]
for i in range(n+1):
	dp[i][0]=i
for i in range(m+1):
	dp[0][i]=i
for i in range(n):
	for j in range(m):
		dp[i+1][j+1]=min(dp[i][j+1]+1,dp[i+1][j]+1,dp[i][j]+int(a[i]!=b[j]))
print(dp[n][m])