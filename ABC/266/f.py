n=int(input())
uv=[[] for i in range(n)]
for i in range(n):
	u,v=map(int,input().split())
	uv[u-1].append(v-1)
	uv[v-1].append(u-1)
loop=[1]*n
nums=[[]]*n
count=1
for i in range(n):
	if len(uv[i])!=1:
		continue
	if not loop[i]:
		continue
	loop[i]=0
	before=i
	ver=uv[i][0]
	while True:
		if loop[ver]==0:
			break
		loop[ver]-=1
		if abs(loop[ver])==len(uv[ver])+1:
			next=uv[ver][0]if uv[ver][1]==before else uv[ver][1]


q=int(input())
for i in range(q):
    x,y=map(int,input().split())