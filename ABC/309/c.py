n,k=map(int,input().split())
ab=[list(map(int,input().split())) for i in range(n)]
ab.sort()
ss=0
for i in range(n):
    a,b=ab[i]
    ss+=b
if ss<=k:
    print(1)
    exit()
for i in range(n):
    a,b=ab[i]
    ss-=b
    if ss<=k:
        print(a+1)
        exit()
