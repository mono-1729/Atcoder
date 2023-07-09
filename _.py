n=int(input())
x=list(map(int,input().split()))
ans=0
mod=10**9+7
dem=[1]
m=x[-1]
for i in range(2,n):
    dem.append((dem[-1]+pow(i,mod-2,mod))%mod)
for i in range(n-1):
    ans+=((x[i+1]-x[i])*dem[i])%mod
    ans%=mod
for i in range(1,n):
    ans*=i
    ans%=mod
print(ans)