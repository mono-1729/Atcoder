from collections import deque
n,m=map(int,input().split())
nm=[[] for i in range(n+m)]
for i in range(n):
	a=int(input())
	s=list(map(int,input().split()))
	for ss in s:
		nm[ss-1].append(m+i)
		nm[m+i].append(ss-1)
que = deque()
que.append((0))
dist = [float('inf')]*(n+m)
dist[0] = 0
while len(que) > 0:
	i= que.popleft()

	d = dist[i] + 1
	for i2 in nm[i]:
		# 暫定距離より短い経路が得られた場合は更新して、+1なら後ろに、+0なら前に付ける

		if d < dist[i2]:
			dist[i2] = d
			que.append(i2)
if dist[m-1]==float('inf'):
	print(-1)
else:
	print(dist[m-1]//2-1)