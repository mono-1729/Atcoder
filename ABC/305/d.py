from bisect import bisect_left,bisect_right
n=int(input())
a=list(map(int,input().split()))
asum=[0]*(n)
for i in range(1,n):
    if i%2==0:
        asum[i]=asum[i-1]+a[i]-a[i-1]
    else:
        asum[i]=asum[i-1]
q=int(input())
for i in range(q):
    l,r=map(int,input().split())
    lbi=bisect_left(a,l)
    rbi=bisect_right(a,r)
    ans=asum[rbi-1]-asum[lbi]
    if lbi%2==0:
        ans+=a[lbi]-l
    if rbi%2==0:
        ans+=r-a[rbi-1]
    print(ans)
    