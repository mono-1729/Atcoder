n=int(input())
t=list(input())
mod=998244353
dp=[[[0,0]for i in range(n+1)] for i in range(n+1)]
dp[0][0]=[0,1]
for i in range(1,2*n+1):
	if t[i-1]=='+':
		for j in range(1,i+1):
			if max(j,i-j)>n or dp[j-1][i-j][1]==0:
				continue
			dp[j][i-j][0]=(dp[j-1][i-j][0]+abs(i-2*j)*dp[j-1][i-j][1])%mod
			dp[j][i-j][1]=dp[j-1][i-j][1]
	if t[i-1]=='-':
		for j in range(1,i+1):
			if max(j,i-j)>n or dp[i-j][j-1][1]==0:
				continue
			dp[i-j][j][0]=(dp[i-j][j-1][0]+abs(i-2*j)*dp[i-j][j-1][1])%mod
			dp[i-j][j][1]=dp[i-j][j-1][1]
	if t[i-1]=='?':
		for j in range(1,i+1):
			if max(j,i-j)<=n and dp[j-1][i-j][1]!=0:
				dp[j][i-j][0]+=dp[j-1][i-j][0]+abs(i-2*j)*dp[j-1][i-j][1]
				dp[j][i-j][1]=(dp[j][i-j][1]+dp[j-1][i-j][1])%mod
				dp[j][i-j][0]%=mod
			if max(j,i-j)<=n and dp[i-j][j-1][1]!=0:
				dp[i-j][j][0]+=dp[i-j][j-1][0]+abs(i-2*j)*dp[i-j][j-1][1]
				dp[i-j][j][1]=(dp[i-j][j][1]+dp[i-j][j-1][1])%mod
				dp[i-j][j][1]%=mod
print(dp[n][n][0])