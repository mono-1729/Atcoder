n=int(input())
a=list(map(int,input().split()))
n3,n2,n1=0,0,0
for i in range(n):
    if a[i]==3:
        n3+=1
    elif a[i]==2:
        n2+=1
    else:
        n1+=1
dp=[[[0]*(n+1) for i in range(n+1)] for j in range(n+1)]
dp[n3][n2][n1]=1
ans=3*n3+2*n2+n1
for i in reversed(range(n+1)):
    for j in reversed(range(n+1)):
        for k in reversed(range(n+1)):
            if dp[i][j][k]==0 or i+j+k==0:
                continue
            ans+=(n/(i+j+k)-1)*dp[i][j][k]
            if i!=0:
                dp[i-1][j+1][k]+=dp[i][j][k]*i/(i+j+k)
            if j!=0:
                dp[i][j-1][k+1]+=dp[i][j][k]*j/(i+j+k)
            if k!=0:
                dp[i][j][k-1]+=dp[i][j][k]*k/(i+j+k) 
print('{:.12f}'.format(ans))