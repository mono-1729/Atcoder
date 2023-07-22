n,d=map(int,input().split())
s=[list(input()) for i in range(n)]
ans=0
num=0
for j in range(d):
    flg=True
    for i in range(n):
        if s[i][j]=='x':
            flg=False
    if flg:
        num+=1
        ans=max(num,ans)
    else:
        num=0
print(ans)