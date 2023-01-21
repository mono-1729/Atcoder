from collections import deque
h,w=map(int,input().split())
s=[list(input()) for i in range(h)]
# 距離＝壁マスを通る回数 として最短路問題を解く。
dist = [[10**9]*w for i in range(h)]
dist[0][0] = 0
 
# dequeを使って01-BFS
que = deque()
que.append((0, 0))
 
while len(que) > 0:
	i, j = que.popleft()
	# 4方向の遷移
	for i2, j2 in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
		if not (0 <= i2 < h and 0 <= j2 < w):
			continue
		# この経路での始点から遷移先までの距離。壁なら+1
		d = dist[i][j]
		if s[i][j] == '#':
			d+=1
		# 暫定距離より短い経路が得られた場合は更新して、+1なら後ろに、+0なら前に付ける
		if d < dist[i2][j2]:
			dist[i2][j2] = d
			if s[i][j] == '#':
				que.append((i2, j2))
			else:
				que.appendleft((i2, j2))
	for i2, j2 in ((i-2, j-1), (i-2, j), (i-2, j+1),(i-1, j-2), (i-1, j-1), (i-1, j+1),(i-1, j+2),(i, j-2), (i, j+2),(i+1, j-2), (i+1, j-1), (i+1, j+1),(i+1, j+2),(i+2, j-1), (i+2, j), (i+2, j+1)):
		if not (0 <= i2 < h and 0 <= j2 < w):
			continue
		# この経路での始点から遷移先までの距離。壁なら+1
		d = dist[i][j]+1
		# 暫定距離より短い経路が得られた場合は更新して、+1なら後ろに、+0なら前に付ける
		if d < dist[i2][j2]:
			dist[i2][j2] = d
			que.append((i2, j2))
print(dist[h-1][w-1])