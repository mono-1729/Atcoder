from collections import deque
n,q=map(int,input().split())
g=[[]for i in range(n+1)]
for i in range(q):
    l,r=map(int,input().split())
    g[l-1].append(r)
    g[r].append(l-1)

dist = [10**9]*(n+1)
dist[0] = 0
que = deque()
que.append(0)

while len(que) > 0:
    i = que.popleft()
    for j in g[i]:
        d = dist[i] + 1
        if d < dist[j]:
            dist[j] = d
            que.append(j)
if dist[-1]==10**9:
    print('No')
else:
    print('Yes')
