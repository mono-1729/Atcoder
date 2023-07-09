n=int(input())
b=[list(input()) for i in range(n)]
ans=[[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        ans[i][j]=b[i][j]
for i in range(1):
    for j in range(n-2*i-1):
        ans[i][i+j+1]=b[i][i+j]
    for j in range(n-2*i-1):
        ans[i+j+1][n-i-1]=b[i+j][n-i-1]
    for j in range(n-2*i-1):
        ans[n-i-1][n-i-j-2]=b[n-i-1][n-i-j-1]
    for j in range(n-2*i-1):
        ans[n-i-j-2][i]=b[n-i-j-1][i]
for i in range(n):
    print(''.join(ans[i]))