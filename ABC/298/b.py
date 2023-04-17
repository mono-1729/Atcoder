n=int(input())
a=[list(map(int,input().split())) for i in range(n)]
b=[list(map(int,input().split())) for i in range(n)]
flg=True
for i in range(n):
    for j in range(n):
        if a[i][j]==1:
            if b[i][j]==0:
                flg=False
if flg:
    print('Yes')
    exit()
flg=True
for i in range(n):
    for j in range(n):
        if a[i][j]==1:
            if b[j][n-1-i]==0:
                flg=False
if flg:
    print('Yes')
    exit()
flg=True
for i in range(n):
    for j in range(n):
        if a[i][j]==1:
            if b[n-1-i][n-1-j]==0:
                flg=False
if flg:
    print('Yes')
    exit()
flg=True
for i in range(n):
    for j in range(n):
        if a[i][j]==1:
            if b[n-1-j][i]==0:
                flg=False
if flg:
    print('Yes')
    exit()
print('No')