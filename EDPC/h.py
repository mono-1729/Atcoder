h,w=map(int,input().split())
a=[input() for i in range(h)]
dp=[0]*w
dp[0]=1
mod=10**9+7
for i in range(h):
    ndp=[0]*w
    for j in range(w):
        if a[i][j]=='#':
            continue
        ndp[j]+=dp[j]
        if j!=0:
            ndp[j]+=ndp[j-1]
        ndp[j]%=mod
    dp=ndp
print(dp[-1])