t=int(input())
for i in range(t):
	n=int(input())
	num=-1
	for j in range(2,int(n**0.5)+2):
		if n%j==0:
			num=j
			break
	if n%(j**2)==0:
		print(f'{j} {n//(j**2)}')
	else:
		print(f'{int(0.5+(n//j)**0.5)} {j}')