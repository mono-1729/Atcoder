n,m,l=map(int,input().split())
edges=[[] for i in range(n)]
for i in range(m):
	a,b,c=map(int,input().split())
	a,b=a-1,b-1
	edges[a].append([b,c])
	edges[b].append([a,c])
dist=[[10**18]*n for i in range(n)]
for i in range(n):
	for b,c in edges[i]:
		dist[i][b]=c
for k in range(n):
	for i in range(n):
		for j in range(n):
			dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
edges2=[[] for i in range(n)]
for i in range(n):
	for j in range(n):
		if dist[i][j]<=l:
			edges2[i].append([j,1])
dist2=[[10**18]*n for i in range(n)]
for i in range(n):
	for b,c in edges2[i]:
		dist2[i][b]=c
for k in range(n):
	for i in range(n):
		for j in range(n):
			dist2[i][j]=min(dist2[i][j],dist2[i][k]+dist2[k][j])
q=int(input())
for i in range(q):
	s,t=map(int,input().split())
	s,t=s-1,t-1
	if dist2[s][t]==10**18:
		print(-1)
	else:
		print(dist2[s][t]-1)