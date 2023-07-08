from collections import defaultdict
n,m=map(int,input().split())
c=list(input().split())
d=defaultdict(int)
dd=list(input().split())
for i,x in enumerate(dd):
    d[x]=i+1
p=list(map(int,input().split()))
ans=0
for i in range(n):
    ans+=p[d[c[i]]]

print(ans)