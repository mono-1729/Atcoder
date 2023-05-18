n=int(input())
mod=998244353
fact=[1 for _ in range(n+1)]
inv=[1 for _ in range(n+1)]
factinv=[1 for _ in range(n+1)]
for i in range(2,n+1):
  fact[i]=(fact[i-1]*i)%mod
  inv[i]=(-inv[mod%i]*(mod//i))%mod
  factinv[i]=(factinv[i-1]*inv[i])%mod
   
def nCk(n,k):
  if n<0 or k<0 or k>n: return 0
  return (fact[n]*factinv[n-k]*factinv[k])%mod

print(nCk(n,n//2))