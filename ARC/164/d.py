n=int(input())
t=list(input())
mod=998244353
fact=[1 for _ in range(2*n+1)]
inv=[1 for _ in range(2*n+1)]
factinv=[1 for _ in range(2*n+1)]
for i in range(2,2*n+1):
	fact[i]=(fact[i-1]*i)%mod
	inv[i]=(-inv[mod%i]*(mod//i))%mod
	factinv[i]=(factinv[i-1]*inv[i])%mod
   
def nCk(n,k):
	if n<0 or k<0 or k>n: return 0
	return (fact[n]*factinv[n-k]*factinv[k])%mod
pcount=0
mcount=0
qcount=0
prob=[[0,0] for i in range(2*n)]
for i in range(2*n):
	if t[i]=='+':
		pcount+=1
	if t[i]=='-':
		mcount+=1
	if t[i]=='?':
		qcount+=1
for i in range(2*n):
	
	prob[i][1]=mod+1-prob[i][0]
dp=[0]*(2*n)
dp2=[]
ans=0
for i in range(1,2*n,2):
	for j in range(0,2*n-i):
		ans+=(1+mod-dp[i])

                
ans=(ans*nCk(qcount,n-pcount))
print(ans)