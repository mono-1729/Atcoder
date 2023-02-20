n,k=map(int,input().split())
a=set(list(map(int,input().split())))
ans=0
for i in range(n):
    if i in a:
        ans+=1
    else:
        break
print(min(ans,k))
