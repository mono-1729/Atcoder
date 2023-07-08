while True:
	n=int(input())
	if n==0:
		exit()
	digit=2
	numsum=0
	while True:
		if numsum+36*(pow(2,digit)-2)+9*(pow(2,digit-1)-1)>=n:
			break
		else:
			numsum+=36*(pow(2,digit)-2)+9*(pow(2,digit-1)-1)
		digit+=1
	ans=[-1]*digit
	ndigit=4*(pow(2,digit)-2)+(pow(2,digit-1)-1)
	num=ndigit
	nums=[-1,-1]
	for i in range(1,10):
		if numsum+ndigit*i>=n:
			ans[0]=i
			numsum+=ndigit*(i-1)
			nums[0]=i
			break
	for i in range(1,digit):
		digitnum=[0]*10
		if nums[1]==-1:
			digitnum=[pow(2,digit-i-1)]*10
			digitnum[nums[0]]=num-9*pow(2,digit-i-1)
		else:
			digitnum[nums[0]]=pow(2,digit-i-1)
			digitnum[nums[1]]=pow(2,digit-i-1)
		for j in range(10):
			if numsum+digitnum[j]>=n:
				ans[i]=j
				num=digitnum[j]
				if nums[0]!=j:
					nums[1]=j
				break
			else:
				numsum+=digitnum[j]
	print(''.join(map(str,ans)))