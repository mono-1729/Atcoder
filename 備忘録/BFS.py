from collections import deque
#計算量：O（V+E）
N = int(input())
E = [[] for _ in range(N)]
for _ in range(N-1):
    A, B = map(int, input().split())
    E[A-1].append(B-1)
    E[B-1].append(A-1)
 
 
def bfs(s):
    dist = [None]*N
    que = deque([s])
    dist[s] = 0
    while que:
        v = que.popleft()
        d = dist[v]
        for w in E[v]:
            if dist[w] is not None:
                continue
            dist[w] = d + 1
            que.append(w)
    d = max(dist)
    return dist.index(d), d
 
 
u, _ = bfs(0)
v, d = bfs(u)
print(d+1)
#01BFS
from collections import deque

# 頂点数N、始点の頂点番号s
N, s = map(int, input().split())
# 隣接リスト。
# edges[i]の要素に(j, c)が含まれる時、iからjにコストcの辺が存在
edges = [[] for i in range(N)]

dist = [10**9]*N
dist[s] = 0
que = deque()
que.append(s)

while len(que) > 0:
    i = que.popleft()
    for j, c in edges[i]:
        d = dist[i] + c
        if d < dist[j]:
            dist[j] = d
            if c == 1:
                que.append(j)
            else:
                que.appendleft(j)

#グリッドグラフ


from collections import deque
 
H, W = map(int, input().split())
C = [input() for i in range(H)]
 
# スタートとゴールを探す
for i in range(H):
    for j in range(W):
        if C[i][j] == 's':
            si, sj = i, j
        if C[i][j] == 'g':
            gi, gj = i, j
 
# 距離＝壁マスを通る回数 として最短路問題を解く。
dist = [[10**9]*W for i in range(H)]
dist[si][sj] = 0
 
# dequeを使って01-BFS
que = deque()
que.append((si, sj))
 
while len(que) > 0:
    i, j = que.popleft()
    
    # 4方向の遷移
    for i2, j2 in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
        if not (0 <= i2 < H and 0 <= j2 < W):
            continue
        # この経路での始点から遷移先までの距離。壁なら+1
        wall = (C[i][j] == '#')
        d = dist[i][j] + wall
 
        # 暫定距離より短い経路が得られた場合は更新して、+1なら後ろに、+0なら前に付ける
        if d < dist[i2][j2]:
            dist[i2][j2] = d
            if wall:
                que.append((i2, j2))
            else:
                que.appendleft((i2, j2))
 
# 終点までの距離が2以下ならYES
if dist[gi][gj] <= 2:
    print("YES")
else:
    print("NO")