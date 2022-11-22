with open('./083/in/90_random_uni_00.txt', mode='r') as f, open('./083/out/90_random_uni_00.txt', mode='r') as g:
	n,m=map(int,f.readline().split())
	ab=[[] for i in range(n+1)]
	hab=[[] for i in range(n+1)]
	hv=set()
	xy=[1]
	last=[0]*(n+1)
	color=[1]*(n+1)
	for i in range(m):
		a,b=map(int,f.readline().split())
		ab[a].append(b)
		ab[b].append(a)
	for i in range(1,n+1):
		if len(ab[i])>(2*m)**0.5:
			hv.add(i)
			for j in ab[i]:
				hab[j].append(i)

	q=int(f.readline())
	for i in range(1,q+1):
		x,y=map(int,f.readline().split())
		if x in hv:
			myans=color[x]
			color[x]=y
		else:
			num=max(last[j] for j in ab[x])
			num=max(num,last[x])
			myans=xy[num]
		ans=int(g.readline().replace('\n',''))
		if myans!=ans:
			print(f'{i} {ans} {myans} {x} {y}')
		xy.append(y)
		last[x]=i
		for k in hab[x]:
			color[k]=y
