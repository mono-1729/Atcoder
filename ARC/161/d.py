n,d=map(int,input().split())
if n*d>(n*(n-1))//2:
	print('No')
	exit()
else:
	print('Yes')
	for i in range(n):
		for j in range(d):
			print(i+1,(i+j+1)%n+1)