n,p,q,r,s=map(int,input().split())
a=list(map(int,input().split()))
b=a.copy()
for i in range(q-p+1):
    b[p-1+i]=a[r-1+i]
    b[r-1+i]=a[p-1+i]
for i in range(n):
    b[i]=str(b[i])
print(" ".join(b))