import time
now=time.time()
from collections import deque
gx,gy=0,0
sx,sy=(300,300)
dist=[[10**9 for _ in range(601)]for _ in range(601)]
dist[sx][sy] = 0
que = deque([(sx,sy)])
while len(que) > 0:
	x, y = que.popleft()
	d = dist[x][y] + 1
	for x2, y2 in ((x+1, y-2), (x+2, y-1), (x+2, y+1), (x+1, y+2), (x-1, y+2), (x-2, y+1), (x-2, y-1),(x-1, y-2)):
		if not (0 <= x2 < 601 and 0 <= y2 < 601):
			continue
		if d < dist[x2][y2]:
			dist[x2][y2] = d
			que.append((x2, y2)) 
print(dist[gx+300][gy+300])
print(time.time()-now)