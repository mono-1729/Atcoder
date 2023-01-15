t=int(input())
for i in range(t):
	n=int(input())
	a=list(map(int,input().split()))
	count=0
	for j in a:
		if j%2==1:
			count+=1
	print(count)