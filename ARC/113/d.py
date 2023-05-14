n,m,k=map(int,input().split())
ans=0
if n==1:
	print(pow(k,m,998244353))
	exit()
if m==1:
	print(pow(k,n,998244353))
	exit()
for i in range(1,k+1):
	ans+=(pow(i,n,998244353)-pow(i-1,n,998244353))*pow(k-i+1,m,998244353)
	ans%=998244353
print(ans)