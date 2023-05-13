from collections import deque

h,w,t=map(int,input().split())
a=[list(input()) for i in range(h)]
dist=[[10**18]*w for i in range(h)]
si=0
sj=0
gi=0
gj=0
oka=[]
for i in range(h):
	for j in range(w):
		if a[i][j]=='S':
			si=i
			sj=j
			oka.append((i,j))
		elif a[i][j]=='G':
			gi=i
			gj=j
for i in range(h):
	for j in range(w):
		if a[i][j]=='o':
			oka.append((i,j))
oka.append((gi,gj))
odist=[[10**18]*len(oka) for i in range(len(oka))]
que = deque()
dist[si][sj] = 0
que.append((si, sj))
 
while len(que) > 0:
    i, j = que.popleft()

    # 4方向の遷移
    for i2, j2 in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
        if (not (0 <= i2 < h and 0 <= j2 < w)) or a[i][j] == '#':
            continue
        d = dist[i][j] + 1

        # 暫定距離より短い経路が得られた場合は更新して、+1なら後ろに、+0なら前に付ける
        if d < dist[i2][j2]:
            dist[i2][j2] = d
            que.append((i2, j2))
for i in range(len(oka)):
	odist[0][i]=dist[oka[i][0]][oka[i][1]]
if dist[gi][gj]>t:
	print('-1')
	exit()
for k in range(1,len(oka)):
	dist=[[10**18]*w for i in range(h)]
	que = deque()
	dist[oka[k][0]][oka[k][1]] = 0
	que.append((oka[k][0], oka[k][1]))
	
	while len(que) > 0:
		i, j = que.popleft()

		# 4方向の遷移
		for i2, j2 in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
			if (not (0 <= i2 < h and 0 <= j2 < w)) or a[i][j] == '#':
				continue
			d = dist[i][j] + 1

			# 暫定距離より短い経路が得られた場合は更新して、+1なら後ろに、+0なら前に付ける
			if d < dist[i2][j2]:
				dist[i2][j2] = d
				que.append((i2, j2))
	for j in range(len(oka)):
		odist[k][j]=dist[oka[j][0]][oka[j][1]]
dp=[[10**18]*(len(oka)-1) for i in range(pow(2,len(oka)-1))]
dp[0][0]=0
kk=[1<<i for i in range(len(oka)-1)]
ans=0
for i in range(pow(2,len(oka)-1)):
	num=bin(i).count('1')
	for j in range(len(oka)-1):
		if dp[i][j]==10**18:
			continue
		for k in range(len(oka)-1):
			if i&kk[k]==0:
				x=i|kk[k]
				dp[x][k]=min(dp[x][k],dp[i][j]+odist[j][k])
		#print(i,j,dp[i][j]+odist[j][-1])
		if dp[i][j]+odist[j][-1]<=t:
			ans=max(ans,num-1)
print(ans)