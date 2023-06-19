h,w=map(int,input().split())
a=[]
b=[]
for i in range(h):
    tmp=list(map(int,input().split()))
    for j in range(w):
        a.append(tmp[j])
for i in range(h):
    tmp=list(map(int,input().split()))
    for j in range(w):
        b.append(tmp[j])
       
dp=[set() for _ in range(w*h)]
dp[0].add(a[0]-b[0])
dp[0].add(-a[0]+b[0])
for i in range(w*h-1):
    for j in dp[i]:
        if i//w!=h-1:
            num=a[i+w]-b[i+w]
            dp[i+w].add(abs(j+num))
            dp[i+w].add(abs(j-num))
        if i%w!=w-1:
            num=a[i+1]-b[i+1]
            dp[i+1].add(abs(j+num))
            dp[i+1].add(abs(j-num))
ans=10**9
for i in dp[w*h-1]:
    ans=min(ans,abs(i))
print(ans)
        