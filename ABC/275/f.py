n,m=map(int,input().split())
a=list(map(int,input().split()))
dp=[[10**5,10**5]for i in range(m+1)]
dp[0][1]=0
for i in range(n):
    ndp=[[10**5,10**5]for i in range(m+1)]
    for j in range(m+1):
        if dp[j][0]!=10**5:
            ndp[j][0]=min(ndp[j][0],dp[j][0])
        if dp[j][1]!=10**5:
            ndp[j][0]=min(ndp[j][0],dp[j][1]+1)
        if j-a[i]>=0 :
            if dp[j-a[i]][0]!=10**5:
                ndp[j][1]=min(ndp[j][1],dp[j-a[i]][0])
            if dp[j-a[i]][1]!=10**5:
                ndp[j][1]=min(ndp[j][1],dp[j-a[i]][1])
    dp=ndp
for i in range(1,m+1):
	ans=min(dp[i][0],dp[i][1]) if min(dp[i][0],dp[i][1])<10**5 else -1
	print(ans)
#print(dp)