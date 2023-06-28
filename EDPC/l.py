n=int(input())
a=tuple(map(int,input().split()))
dp=[[0 for i in range(n+1)]for i in range(n+1)]
mod=n%2
for i in range(1,n+1):
	for j in range(0,n+1-i):
		if i%2==mod:
			dp[j][j+i]=max(dp[j][j+i-1]+a[j+i-1],dp[j+1][j+i]+a[j])
		else:
			dp[j][j+i]=min(dp[j][j+i-1]-a[j+i-1],dp[j+1][j+i]-a[j])
print(dp[0][n])