n,k,m=map(int,input().split())
mod=998244353
if m%mod==0:
    print(0)
    exit()
print(pow(m%mod,pow(k%(mod-1),n,mod-1),mod))
print(pow(pow(m%mod,k,mod),n,mod))
print(2**18)