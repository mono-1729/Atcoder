from math import gcd
n=int(input())
ab=[]
for i in range(n):
    a,b=map(int,input().split())
    g=gcd(a,b+a)
    ab.append(((a//g)*(10**24)//((a+b)//g),-i))
ab.sort(reverse=True)
ans=[]
for i in range(n):
    #print(ab[i])
    ans.append(str(-ab[i][1]+1))
print(' '.join(ans))