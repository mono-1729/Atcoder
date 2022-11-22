n=int(input())
w=list(map(int,input().split()))
b=list(map(int,input().split()))
g=[[0 for i in range(1600)]for j in range(51)]
for i in range(51):
  for j in range(1500):
    mex=[0 for k in range(1500)]
    if i>=1:
      mex[g[i-1][j+i]]=1
    if j>=2:
      for k in range(1,j//2+1):
        mex[g[i][j-k]]=1
    for k in range(1500):
      if mex[k]==0:
        g[i][j]=k
        break
ans=0
for i in range(n):
  ans^=g[w[i]][b[i]]
if ans==0:
  print("Second")
else:
  print("First")