D=int(input())
p=998244353
fact=[1 for _ in range(2*D+1)]
inv=[1 for _ in range(2*D+1)]
factinv=[1 for _ in range(2*D+1)]
for i in range(2,2*D+1):
  fact[i]=(fact[i-1]*i)%p
  inv[i]=(-inv[p%i]*(p//i))%p
  factinv[i]=(factinv[i-1]*inv[i])%p
   
def nCk(n,k):
  if n<0 or k<0 or k>n: return 0
  return (fact[n]*factinv[n-k]*factinv[k])%p

print(nCk(2*D-1,D))