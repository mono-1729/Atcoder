n,m=map(int,input().split())
b=[0]*n
dp=[0]*(1<<n)
dp[0]=1
for i in range(m):
	x,y=map(int,input().split())
	x-=1
	y-=1
	b[x]|=1<<y
jbs = [(j, 1 << j) for j in range(n)]
for i in range(1<<n):
	for j, jb in jbs:
		if (i & jb) == 0 and (i & b[j]) == 0:
			dp[i | jb] += dp[i]
print(dp[-1])
