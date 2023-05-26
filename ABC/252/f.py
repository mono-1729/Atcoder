import heapq
n,l=map(int,input().split())
a=list(map(int,input().split()))
ans=0
if sum(a)<l:
    a.append(l-sum(a))
heapq.heapify(a)
while len(a)>1:
	x=heapq.heappop(a)
	y=heapq.heappop(a)
	ans+=x+y
	heapq.heappush(a,x+y)
print(ans)
