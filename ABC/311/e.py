h,w,n=map(int,input().split())
dp=[[0]*(w+1) for i in range(h+1)]
ab=set([tuple(map(int,input().split())) for i in range(n)])
for i in range(1,h+1):
    for j in range(1,w+1):
        if (i,j) not in ab:
            dp[i][j]+=1
            dp[i][j]+=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
print(sum([sum(dp[i]) for i in range(h+1)]))
            