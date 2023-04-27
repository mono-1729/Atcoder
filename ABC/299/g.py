from heapq import heappop,heappush
from collections import defaultdict
n,m=map(int,input().split())
a=list(map(int,input().split()))
q=[]
flag=[0]*(m+1)
d=defaultdict(int)
for num in a:
    d[num]+=1
ans=[]
prev=-1
for i in range(n):
    num=a[i]
    d[num]-=1
    if flag[num]:
        continue
    heappush(q,(num,i))
    if d[num]==0:
        while q:
            if num<q[0][0]:
                break
            nn,j=heappop(q)
            if flag[nn]:
                continue
            if prev<j:
                ans.append(nn)
                prev=j
                flag[nn]=True
print(*ans)