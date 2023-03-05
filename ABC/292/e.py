n,m=map(int,input().split())
uv=[set() for i in range(n)]
for i in range(m):
    u,v=map(int,input().split())
    uv[u-1].add(v-1)
ans=0
for i in range(4*n):
	x=list(uv[i%n])
	for j in x:
		for k in uv[j]:
			if not k in uv[i%n]:
				if i%n!=k:
					uv[i%n].add(k)
					#print(i%n,k)
					ans+=1
print(ans)
