from collections import deque
n,m=map(int,input().split())
uv=[[] for i in range(n)]
col=[None]*n
for i in range(m):
    u,v=map(int,input().split())
    uv[u-1].append(v-1)
    uv[v-1].append(u-1)
k=int(input())
pos=[[] for i in range(n)]
pd=[]
for i in range(k):
	dist=[10**9]*n
	p,d=map(int,input().split())
	p-=1
	pd.append([p,d])
	if d==0:
		col[p]=1
		continue
	else:
		col[p]=0
	que=deque()
	que.append((p,1))
	while len(que) > 0:
		a,b = que.popleft()
		for j in uv[a]:
			if b==d:
				pos[p].append(j)
				continue
			else:
				if col[j]==1:
					print('No')
					exit()
				else:
					col[j]=0
			dd = b + 1
			if dd < dist[j] :
				dist[j] = dd
				que.append((j,b+1))
if not (1 in col or None in col):
	print('No')
	exit()
for i in range(k):
	p,d=pd[i]
	flg=True
	if d==0:
		continue
	else:
		for j in pos[p]:
			if col[j]!=0:
				flg=False
				break
		if flg:
			print('No')
			exit()
for i in range(n):
	if col[i]==None:
		col[i]=1
print('Yes')
print(''.join(list(map(str,col))))