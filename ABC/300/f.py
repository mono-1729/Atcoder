from bisect import bisect_right
n,m,k=map(int,input().split())
s=list(input())
t=s+s
num=[0]*(2*n+1)
count=0
for i in range(n):
    if s[i]=='x':
        count+=1
        num[i+1]=1
        num[n+i+1]=1
for i in range(2*n):
    num[i+1]+=num[i]
if k<count:
	ans=0
	if m-1==0:
		for i in range(n):
			ans=max(ans,min(bisect_right(num,num[i]+k),n)-i-1)
	else:
		for i in range(n):
			ans=max(ans,bisect_right(num,num[i]+k)-i-1)
	print(min(ans,n*m))
else:
	x=n*(k//count)
	z=k//count
	ans=0
	k%=count
	cc=num[n]
	if m-1==z:
		for i in range(n+1):
			ans=max(ans,min(bisect_right(num,num[i]+k),n)-i-1)
	else:
		for i in range(n+1):
			ans=max(ans,bisect_right(num,num[i]+k)-i-1)
	print(min(x+ans,n*m))
    
