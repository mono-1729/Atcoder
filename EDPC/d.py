n,w=map(int,input().split())
dp=[0]*(w+1)
for i in range(n):
    ww,v=map(int,input().split())
    ndp=[0]*(w+1)
    for j in range(1,w+1):
        if j-ww>=0:
            ndp[j]=dp[j-ww]+v
        ndp[j]=max(ndp[j],dp[j])
    dp=ndp
print(dp[w])