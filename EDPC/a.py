n=int(input())
h=list(map(int,input().split()))
dp=[10**10 for i in range(n)]
dp[0]=0
for i in range(n):
    if i+1<n:
        dp[i+1]=min(dp[i+1],dp[i]+abs(h[i]-h[i+1]))
    if i+2<n:
        dp[i+2]=min(dp[i+2],dp[i]+abs(h[i]-h[i+2]))
print(dp[n-1])
    