n,q=map(int,input().split())
uv=[set() for i in range(n)]
num=n
for i in range(q):
	query=list(map(int,input().split()))
	if query[0]==1:
		_,u,v=query
		u-=1
		v-=1
		if len(uv[u])==0:
			num-=1
		if len(uv[v])==0:
			num-=1
		uv[u].add(v)
		uv[v].add(u)
	else:
		_,v=query
		v-=1
		#print(uv[v].a)
		for x in uv[v]:
			if len(uv[x])==1:
				num+=1
			uv[x].remove(v)
		if len(uv[v])>0:
			num+=1
		uv[v]=set()
	print(num)
