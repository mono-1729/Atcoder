from collections import defaultdict
n=int(input())
q=int(input())
a=[set() for i in range(2*10**5+1)]
l=[[] for i in range(n+1)]
for _ in range(q):
    query=list(map(int,input().split()))
    if query[0]==1:
        _,i,j=query
        a[i].add(j)
        l[j].append(i)
    if query[0]==2:
        _,i=query
        l[i].sort()
        print(*l[i])
    if query[0]==3:
        _,i=query
        aa=sorted(list(a[i]))
        print(*aa)