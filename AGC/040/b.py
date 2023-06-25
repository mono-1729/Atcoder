n=int(input())
lr=[tuple(map(int,input().split())) for _ in range(n)]
rl=[]
ans=0
rmin=10**9
lmax=0
rlmax=0
for l,r in lr:
    rmin=min(rmin,r)
    lmax=max(lmax,l)
    rlmax=max(rlmax,r-l)
ans=max(ans,rlmax+1+max(0,rmin-lmax+1))
num1=[10**9]*(n+1)
num2=[10**9]*(n+1)
lr.sort(reverse=True)
for i in range(n):
    l,r=lr[i]
    num1[i+1]=min(num1[i],max(0,r-lmax+1))
for i in range(n):
	l,r=lr[n-i-1]
	num2[i+1]=min(num2[i],max(0,rmin-l+1))
for i in range(1,n):
	ans=max(ans,num1[i]+num2[n-i])
	#print(ans,i,num1[i],num2[n-i])
print(ans)