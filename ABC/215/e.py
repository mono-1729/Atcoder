n=int(input())
s=input()
dp=[[[0]*10 for i in range(1<<10)] for _ in range(n+1)]
for i in range(n):
	num=ord(s[i])-ord('A')
	dp[i+1][1<<num][num]+=1
	for j in range(1<<10):
		for k in range(10):
			dp[i+1][j][k]=(dp[i+1][j][k]+dp[i][j][k])%998244353
			if k==num or not (j>>num &1):
				dp[i+1][j|(1<<num)][num]+=dp[i][j][k]

print(sum(sum(dp[n][j]) for j in range(1,1<<10))%998244353)
