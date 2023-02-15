n,k=map(int,input().split())
a=list(map(int,input().split()))
mod=998244353

def comb(n,r):
    a=1
    for i in range(r):
        a=(a*(n-i))%mod
    b=1
    for i in range(r):
        b=(b*(i+1))%mod
    return (a*pow(b,mod-2,mod))%mod

aa=a[0]-sum(a[1:])-k

if aa<0:
    print(0)
else:
    ans=1
    for i in range(1,n):
        ans=(ans*comb(a[i]+k-1,k-1))%mod
    ans=(ans*comb(aa+k-1,k-1))%mod
    print(ans)