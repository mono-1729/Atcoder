from collections import defaultdict
n,k=map(int,input().split())
a=list(map(int,input().split()))
m=defaultdict(int)
r=0
c=0
ans=0
for i in range(n):
  while r<=n-1:
    if m[a[r]]==0 and  c==k:
      break
    if m[a[r]]==0:
      c+=1
    m[a[r]]+=1
    r+=1
  ans=max(ans,r-i)
  if m[a[i]]==1:
    c-=1
  m[a[i]]-=1
print(ans)