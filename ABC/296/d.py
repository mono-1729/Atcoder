n,m=map(int,input().split())
ans=10**20
for i in range(min(n+1,10**6+2)):
    if i*n>=m:
        ans=min(ans,i*(((m-1)//i)+1))
if ans>10**12:
    print(-1)
else:
    print(ans)