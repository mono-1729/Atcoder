n=int(input())
a=[list(map(int,input().split())) for i in range(n)]
ans=0
for i in range(n):
    for j in range(i):
        ans+=a[i][j]

for i in range(n-1):
	for j in range(i,n):
		flg=False
		for k in range(n):
			if a[i][j]>a[i][k]+a[k][j]:
				print(-1)
				exit()
			if a[i][j]==a[i][k]+a[k][j] and k!=i and k!=j:
				flg=True
		if flg:
			ans-=a[i][j]
print(ans)