n,k=map(int,input().split())
a=list(map(int,input().split()))
s=sum(a)
nums=[]
ans=1
for i in range(1,int(s**0.5)+2):
	if s%i==0:
		nums.append(i)
		nums.append(s//i)
for i in nums:
	count1=0
	count2=0
	x=[a[j]%i for j in range(n)]
	x.sort()
	c1=0
	c2=n-1
	for j in range(n):
		if count1 < count2:
			count1 += x[c1]
			c1 += 1
		else:
			count2 += i-x[c2]
			c2-=1
	if max(count2,count1)<=k:
		ans=max(ans,i)
print(ans)