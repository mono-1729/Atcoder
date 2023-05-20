from bisect import bisect_left,bisect_right
n,m,d=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort()
b.sort()
ans=-1
for i in range(n):
	index=bisect_right(b,a[i]+d)
	if index==0:
		continue
	if abs(a[i]-b[index-1])<=d:
		ans=max(ans,a[i]+b[index-1])
print(ans)