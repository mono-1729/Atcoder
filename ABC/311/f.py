n,m=map(int,input().split())
s=[list(input()) for i in range(n)]
mod=998244353
for i in range(n):
	for j in range(m):
		if s[i][j]=='#':
			if i!=n-1:
				s[i+1][j]='#'
				if j!=m-1:
					s[i+1][j]='#'
dp=[[[0,0]for i in range(m+1)] for i in range(n+1)]
for i in range(m+1):
	dp[n][i][1]=1
for i in range(n+1):
	dp[i][m][1]=1
for i in reversed(range(m)):
	for j in reversed(range(m)):
		dp[i][j][1]=((dp[i+1][j][1]*dp[i][j+1][1])//dp[i+1][j+1][1])%mod
		if s[i][j]=='.':
			dp[i][j][0]=dp[i][j][1]
		else:
			dp[i][j][0]=((dp[i+1][j][0]*dp[i][j+1][0])//dp[i+1][j+1][0])%mod
print(sum(dp[0][0]))
print(dp)