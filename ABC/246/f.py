n,l=map(int,input().split())
s=[set(list(input())) for _ in range(n)]
mod=998244353
ans=0
nums={}
chars=set(chr(i) for i in range(ord('a'),ord('z')+1))
for i in range(1,1<<n):
	ch=chars.copy()
	count=0
	for j in range(n):
		if i&(1<<j):
			ch&=set(s[j])
			count+=1
	nums[i]=(pow(len(ch),l,mod),count)
for i in range(n):
	for j in range(1<<i,1<<(i+1)):
		num,count=nums[j]
		if count%2==0:
			ans-=num
		else:
			ans+=num
		ans%=mod
print(ans)