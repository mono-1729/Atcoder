n,k=map(int,input().split())
a=list(map(int,input().split()))
aa=a.copy()
x=int(input())
for i in range(x,n-k+1):
    num=aa[i]
    for j in range(1):
        aa[i+1+j]-=num
l=aa[n-k:]
print(aa)