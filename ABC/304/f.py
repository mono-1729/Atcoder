n=int(input())
s=list(input())
num1=2
ans=0
mod=998244353
for i in range(n):
	if s[i]=='.':
		num1=1
		break
ans+=num1
mlist=[]
tmp=n
for i in range(2,int(n**(1/2))+1):
	if tmp%i==0:
		mlist.append(i)
		mlist.append(tmp//i)
nums=[0]*(len(mlist)+1)
nums[0]=num1
mlist=list(set(mlist))
mlist.sort()
for i in range(len(mlist)):
	m=mlist[i]
	yaku=[0]
	for j in range(i):
		if m%mlist[j]==0:
			yaku.append(j+1)
	check=[0]*m
	for j in range(n):
		if s[j]=='.':
			check[j%m]=1
	num=m-sum(check)
	x=pow(2,num,mod)
	for j in range(len(yaku)):
		x-=nums[yaku[j]]
		x%=mod
	nums[i+1]=x
	ans+=x
	ans%=mod
	# print(ans)
	# print(nums)
	# print(check)
	# print(yaku)
print(ans%mod)
#print(mlist)