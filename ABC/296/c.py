from collections import defaultdict
d=defaultdict(int)
n,x=map(int,input().split())
if x==0:
    print('Yes')
    exit()
a=list(map(int,input().split()))
for i in range(n):
    if d[a[i]+x]!=0 or d[a[i]-x]!=0:
        print('Yes')
        exit()
    d[a[i]]+=1
print('No')
