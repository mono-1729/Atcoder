n,m,k=map(int,input().split())
a=list(map(int,input().split()))
ans=0
for i in reversed(range(31)):
	ans+=1<<i
	numlist=[]
	for j in range(n):
		for bit in reversed(range(32)):
			if (1<<bit) & ans &(~a[j]):
				numlist.append(ans%(1<<(bit+1))-a[j]%(1<<(bit+1)))
				break
			if bit==0:
				numlist.append(0)
	# print(numlist)
	numlist.sort()
	if sum(numlist[:k])>m:
		ans-=1<<i
	# print(ans)
print(ans)