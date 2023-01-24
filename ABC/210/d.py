h,w,c=map(int,input().split())
a=[list(map(int,input().split())) for i in range(h)]
dp=[[10**10]*(w+1) for i in range(h+1)]
ans=10**10
for i in range(1,h+1):
    for j in range(1,w+1):
        num=min(dp[i-1][j]+c,dp[i][j-1]+c)
        ans=min(ans,num+a[i-1][j-1])
        dp[i][j]=min(a[i-1][j-1],num)
dp=[[10**10]*(w+1) for i in range(h+1)]
for i in range(1,h+1):
    for j in reversed(range(w)):
        num=min(dp[i-1][j]+c,dp[i][j+1]+c)
        ans=min(ans,num+a[i-1][j])
        dp[i][j]=min(a[i-1][j],num)
print(ans)