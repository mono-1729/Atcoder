#典型28
n=int(input())
cumsum = [[0] * 1002 for i in range(1002)]
for i in range(n):
  lx,ly,rx,ry=map(int,input().split())
  cumsum[lx][ry]+=1
  cumsum[lx][ly]-=1
  cumsum[rx][ry]-=1
  cumsum[rx][ly]+=1
for y in range(1002):
  for x in range(1001):
    cumsum[y][x+1] += cumsum[y][x]
for x in range(1002):
  for y in range(1001):
    cumsum[y+1][x] += cumsum[y][x]
print(cumsum)
