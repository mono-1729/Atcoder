from bisect import *
from collections import defaultdict
w,h=map(int,input().split())
n=int(input())
pq=[list(map(int,input().split())) for i in range(n)]
alen=int(input())
a=list(map(int,input().split()))
blen=int(input())
b=list(map(int,input().split()))
itigo=defaultdict(int)
num=0
maxnum=0
minnum=10**9
for p,q in pq:
	x=bisect_left(a,p)
	y=bisect_left(b,q)
	if itigo[(x,y)]==0:
		num+=1
	itigo[(x,y)]+=1
	maxnum=max(maxnum,itigo[(x,y)])
for p,q in pq:
	x=bisect_left(a,p)
	y=bisect_left(b,q)
	minnum=min(minnum,itigo[(x,y)])
if num<(alen+1)*(blen+1):
	minnum=0
print(minnum,maxnum)


