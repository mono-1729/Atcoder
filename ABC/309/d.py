from collections import deque
n1,n2,m=map(int,input().split())
edge1=[[] for i in range(n1)]
edge2=[[] for j in range(n2)]
ans=1
for i in range(m):
	a,b=map(int,input().split())
	if b<=n1:
		a,b=a-1,b-1
		edge1[a].append(b)
		edge1[b].append(a)
	else:
		a,b=a-n1-1,b-n1-1
		edge2[a].append(b)
		edge2[b].append(a)
dist = [None]*n1
que = deque([0])
dist[0] = 0
while que:
	v = que.popleft()
	d = dist[v]
	for w in edge1[v]:
		if dist[w] is not None:
			continue  
		dist[w] = d + 1
		que.append(w)
ans+=max(dist)
dist = [None]*n2
que = deque([n2-1])
dist[n2-1] = 0
while que:
	v = que.popleft()
	d = dist[v]
	for w in edge2[v]:
		if dist[w] is not None:
			continue  
		dist[w] = d + 1
		que.append(w)
ans+=max(dist)
print(ans)