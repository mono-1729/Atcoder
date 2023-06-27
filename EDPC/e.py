n,w=map(int,input().split())
dp=[10**10]*(10**5+1)
dp[0]=0
for i in range(n):
	ww,v=map(int,input().split())
	ndp=[10**10]*(10**5+1)
	ndp[0]=0
	for j in range(1,10**5+1):
		ndp[j]=dp[j]
		if j-v>=0:
			ndp[j]=min(ndp[j],dp[j-v]+ww)
	dp=ndp
for i in reversed(range(10**5+1)):
	if dp[i]<=w:
		print(i)
		exit()
