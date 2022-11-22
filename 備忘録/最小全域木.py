from heapq import heappush, heappop
 
n, m = map(int, input().split())
 
graph = [[] for _ in range(n)]
ans=[]
 
for x in range(m):
  u, v, c = map(int, input().split())
 
  graph[u-1].append([v-1, c,x+1]) # u->vの辺
  graph[v-1].append([u-1, c,x+1]) # v->uの辺
 
marked = [False for _ in range(n)]
# マークされている頂点数を数える
marked_cnt = 0
marked[0] = True
marked_cnt += 1
q = []
for j, c,x in graph[0]:
  heappush(q, [c, j,x])
total = 0
 
# すべての頂点をマークするまでwhileループ
while marked_cnt < n:
  # 最小の重みの辺をheapで取り出す
  c, i,x = heappop(q)
 
  # マークされているならスキップ
  if marked[i]:
    continue
 
  # 頂点をマーク
  marked[i] = True
  marked_cnt += 1
  total += c
  ans.append(str(x))
  # 頂点iに隣接する辺を保存
  for j, c,x in graph[i]:
  # マークされていればスキップ
    if marked[j]:
      continue
    heappush(q, [c, j,x])
 
print(' '.join(ans))