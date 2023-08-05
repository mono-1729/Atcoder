s=list(input())
dp=[[0]*3001 for i in range(len(s)+1)]
dp[0][0]=1
mod=998244353
for i in range(len(s)):
	for j in range(3001):
		if s[i]=='(':
			if j!=3000:
				dp[i+1][j+1]+=dp[i][j]
				dp[i+1][j+1]%=mod
		if s[i]==')':
			if j!=0:
				dp[i+1][j-1]+=dp[i][j]
				dp[i+1][j-1]%=mod
		if s[i]=='?':
			if j!=3000:
				dp[i+1][j+1]+=dp[i][j]
				dp[i+1][j+1]%=mod
			if j!=0:
				dp[i+1][j-1]+=dp[i][j]
				dp[i+1][j-1]%=mod
print(dp[len(s)][0])
        