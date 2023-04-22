n,t=map(int,input().split())
c=list(map(int,input().split()))
r=list(map(int,input().split()))
cc=c[0]
num=0
ans=1
if t in c:
	for i in range(n):
		if c[i]==t:
			if num<r[i]:
				num=r[i]
				ans=i+1
else:
	for i in range(n):
		if c[i]==c[0]:
			if num<r[i]:
				num=r[i]
				ans=i+1
print(ans)