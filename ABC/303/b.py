n,m=map(int,input().split())
a=[list(map(int,input().split())) for i in range(m)]
ans=0
for i in range(1,n+1):
	for j in range(i+1,n+1):
		flg=True
		for k in range(m):
			for l in range(n-1):
				if (a[k][l] in {i,j}) and (a[k][l+1] in {i,j}):
					flg=False
		if flg:
			ans+=1
print(ans)