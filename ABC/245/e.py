n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
d=list(map(int,input().split()))
choco=[(a[i],b[i]) for i in range(n)]
box=[(c[i],d[i]) for i in range(m)]
choco.sort()
box.sort()
count=0

for i in range(n):
    
