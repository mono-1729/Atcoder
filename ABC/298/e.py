n,a,b,p,q=map(int,input().split())
mod=998244353
ans=0
mods=[pow(i,mod-2,mod)for i in range(11)]
takahashi=[0]*(n)
aoki=[0]*(n)
takahashi[a]=1
aoki[b]=1
takahashi_count=[0]*(n+1)
aoki_count=[0]*(n+1)
for i in range(1,n-a+1):
	for j in reversed(range(a,n)):
		for k in range(1,p+1):
			if j+k>=n:
				takahashi_count[i]=(takahashi_count[i]+takahashi[j]*mods[p])%mod
			else:
				takahashi[j+k]=(takahashi[j+k]+takahashi[j]*mods[p])%mod
		takahashi[j]=0
for i in range(1,n-b+1):
	for j in reversed(range(b,n)):
		for k in range(1,q+1):
			if j+k>=n:
				aoki_count[i]=(aoki_count[i]+aoki[j]*mods[q])%mod
			else:
				aoki[j+k]=(aoki[j+k]+aoki[j]*mods[q])%mod
		aoki[j]=0
for i in reversed(range(n)):
	aoki_count[i]=(aoki_count[i+1]+aoki_count[i])%mod
for i in range(1,n+1):
	ans=(ans+takahashi_count[i]*aoki_count[i])%mod
print(ans)
