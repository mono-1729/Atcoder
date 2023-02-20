n,m=map(int,input().split())
s=list(input())
now=n
ans=[]
while True:
    flag=True
    if now<=m:
        ans.append(now)
        break
    for i in reversed(range(1,m+1)):
        if s[now-i]=='0':
            flag=False
            ans.append(i)
            now-=i
            break
    if flag:
        print(-1)
        exit()
print(' '.join(reversed(list(map(str,ans)))))