n,q=map(int,input().split())
c=[0]*(n+1)
for i in range(q):
    num,x=map(int,input().split())
    if num<=2:
        c[x]+=num
    else:
        if c[x]>=2:
            print('Yes')
        else:
            print('No')