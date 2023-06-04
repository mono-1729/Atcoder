n=int(input())
if n<10**3:
    print(n)
else:
	for i in range(4,10):
		if n<10**i:
			print(n-n%(10**(i-3)))
			exit()