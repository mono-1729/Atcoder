while True:
	n,m=map(int,input().split())
	if n==m==0:
		exit()
	minp=[[0,i] for i in range(n)]
	maxp=[[0,i] for i in range(n)]
	for i in range(m):
		skc=list(map(int,input().split()))
		s,k,c=skc[0],skc[1],skc[2:]
		if k==1:
			minp[c[0]-1][0]+=s
		for cc in c:
			maxp[cc-1][0]+=s
	minp.sort()
	maxp.sort(reverse=True)
	if minp[0][1]==maxp[0][1]:
		print(max(maxp[0][0]-minp[1][0]+1,maxp[1][0]-minp[0][0]+1))
	else:
		print(maxp[0][0]-minp[0][0]+1)