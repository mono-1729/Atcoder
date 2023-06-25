n=int(input())
a=list(map(int,input().split()))
x=[]
for i in range(n):
    ans=0
    for j in range(7):
        ans+=a[i*7+j]
    x.append(str(ans))
print(' '.join(x))
