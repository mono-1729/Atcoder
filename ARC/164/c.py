import heapq
n=int(input())
ab=[list(map(int,input().split())) for i in range(n)]
card=[]
ans=0
for i in range(n):
    a,b=ab[i]
    heapq.heappush(card,[b-a,i,0])
for i in range(n):
    num,x,y=heapq.heappop(card)
    heapq.heappush(card,[-num,x,1-y])
    num,x,y=heapq.heappop(card)
    ans+=ab[x][y]
print(ans)