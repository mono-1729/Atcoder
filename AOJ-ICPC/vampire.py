while True:
	r,n=map(int,input().split())
	if r==0 and n==0:
		exit()
	t=[0]*40
	for i in range(n):
		ll,rr,h=map(int,input().split())
		for j in range(ll+20,rr+20):
			t[j]=max(t[j],h)
	ans=10**10
	for i in range(40):
		pos=i%20
		if i<20:
			pos=abs(i-19)
		if pos>=r:
			continue
		ans=min(ans,t[i]+r-(r**2-pos**2)**0.5)
	print('{:.12f}'.format(ans))