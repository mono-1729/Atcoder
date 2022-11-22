n,p,k=map(int,input().split())
a=[list(map(int,input().split()))for i in range(n)]
dist=[[1]*n for i in range(n)]
for i in range(n):
  for j in range(n):
    dist[i][j]=a[i][j]
for k in range(n):
  for i in range(n):
    for j in range(n):
      dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])