l=list(input())
ans=1
num=0
ll=len(l)
mod=10**9+7
for i in range(ll):
    if l[i]=='1':
        ans=(ans+pow(2,num,mod)*(pow(3,ll-i-1,mod)+1))%mod
        num+=1
print(ans)