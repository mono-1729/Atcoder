n=int(input())
a=list(map(int,input().split()))
s=[list(input()) for i in range(n)]
q=int(input())
dist=[[(1<<20,0)for i in range(n)] for i in range(n)]
for i in range(n):
	for j in range(n):
		if s[i][j]=='Y':
			dist[i][j]=(1,a[i])
for k in range(n):
	for i in range(n):
		for j in range(n):
			if dist[i][j][0]>dist[i][k][0]+dist[k][j][0]:
				dist[i][j]=(dist[i][k][0]+dist[k][j][0],dist[i][k][1]+dist[k][j][1])
			elif dist[i][j][0]==dist[i][k][0]+dist[k][j][0]:
				dist[i][j]=(dist[i][j][0],max(dist[i][j][1],dist[i][k][1]+dist[k][j][1]))
for i in range(q):
	u,v=map(int,input().split())
	if dist[u-1][v-1][0]==1<<20:
		print('Impossible')
	else:
		print(f"{dist[u-1][v-1][0]} {dist[u-1][v-1][1]+a[v-1]}")