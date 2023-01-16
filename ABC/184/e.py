from collections import deque,defaultdict
h,w=map(int,input().split())
a=[list(input()) for i in range(h)]
tel=defaultdict(list)
for i in range(h):
	for j in range(w):
		if a[i][j] == 'S':
			si, sj = i, j
		elif a[i][j] == 'G':
			gi, gj = i, j
		elif a[i][j]!='.' and a[i][j]!='#':
			tel[a[i][j]].append((i,j))
# 距離＝壁マスを通る回数 として最短路問題を解く。
dist = [[10**9]*w for i in range(h)]
dist[si][sj] = 0
# dequeを使って01-BFS
que = deque()
que.append((si, sj))
while len(que) > 0:
	i, j = que.popleft()
	if tel[a[i][j]]!=[]:
		for i2, j2 in tel[a[i][j]]:
			if not (0 <= i2 < h and 0 <= j2 < w) or a[i][j] == '#':
				continue
			if i==i2 and j==j2 :
				continue
			d = dist[i][j] + 1
			# 暫定距離より短い経路が得られた場合は更新して、+1なら後ろに、+0なら前に付ける
			if d < dist[i2][j2]:
				dist[i2][j2] = d
				que.append((i2, j2))
		tel[a[i][j]]=[]
	# 4方向の遷移
	for i2, j2 in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
		if not (0 <= i2 < h and 0 <= j2 < w) or a[i][j] == '#':
			continue
		d = dist[i][j] + 1
		# 暫定距離より短い経路が得られた場合は更新して、+1なら後ろに、+0なら前に付ける
		if d < dist[i2][j2]:
			dist[i2][j2] = d
			que.append((i2, j2))
ans=-1 if dist[gi][gj]==10**9 else dist[gi][gj]
print(ans)