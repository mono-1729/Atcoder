n,k=map(int,input().split())
x=list(map(int,input().split()))
active=[0]*(n+1)
num=0
for i in range(k):
    active[x[i]]=i+1
    num=max(num,x[i])
print(active[num])
for i in range(k,n):
	active[x[i]]=i+1
	if num>x[i]:
		while True:
			num-=1
			if active[num]!=0:
				break
	print(active[num])