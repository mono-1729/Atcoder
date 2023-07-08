import heapq
n,m=map(int,input().split())
p=list(map(int,input().split()))
l=list(map(int,input().split()))
d=list(map(int,input().split()))
ld=[(l[i],d[i]) for i in range(m)]
p.sort()
ld.sort()
ave=[]
ans=sum(p)
count=0
for i in range(n):
    while count<m and ld[count][0]<=p[i]:
        heapq.heappush(ave,-ld[count][1])
        count+=1
    if len(ave)>0:
        x=heapq.heappop(ave)
        ans+=x
        #print(x)
print(ans)
        

