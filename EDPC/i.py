n=int(input())
p=list(map(float,input().split()))
dp=[0]*(n+1)
dp[0]=1
for i in range(n):
    ndp=[0]*(n+1)
    for j in range(n):
        ndp[j+1]+=dp[j]*p[i]
        ndp[j]+=dp[j]*(1-p[i])
    dp=ndp
ans=0
for i in range(n//2+1,n+1):
    ans+=dp[i]
print('{:.12f}'.format(ans))