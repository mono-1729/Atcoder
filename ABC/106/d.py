n,m,q=map(int,input().split())
cnt=[[0]*(n+1)for i in range(n+1)]
for i in range(m):
	l,r=map(int,input().split())
	cnt[l][r]+=1
for i in range(1,n+1):
	for j in range(i,n+1):
		cnt[i][j]+=cnt[i][j-1]
for i in range(q):
	p,q=map(int,input().split())
	ans=0
	for j in range(p,q+1):
		ans+=cnt[j][q]
	print(ans)