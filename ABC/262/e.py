n,m,k=map(int,input().split())
p=998244353
fact=[1 for _ in range(n+1)]
inv=[1 for _ in range(n+1)]
factinv=[1 for _ in range(n+1)]
for i in range(2,n+1):
  fact[i]=(fact[i-1]*i)%p
  inv[i]=(-inv[p%i]*(p//i))%p
  factinv[i]=(factinv[i-1]*inv[i])%p
   
def nCk(n,k):
  if n<0 or k<0 or k>n: return 0
  return (fact[n]*factinv[n-k]*factinv[k])%p
uv=[[] for i in range(n)]
for i in range(m):
	u,v=map(int,input().split())
	uv[u-1].append(v-1)
	uv[v-1].append(u-1)
uvnum=[len(uv[i]) for i in range(n)]
even=0
odd=0
ans=0
for i  in range(n):
	if uvnum[i]%2==0:
		even+=1
	else:
		odd+=1
for i in range(0,min(k,odd)+1,2):
	ans+=nCk(odd,i)*nCk(even,k-i)
	ans%=p
print(ans)