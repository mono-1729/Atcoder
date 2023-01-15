h,w=map(int,input().split())
cumsum = [[[0,0] for i in range(w)]  for i in range(h)]
# for i in range(h):
# 	for j in range(w):
# 		cumsum[i][j]=[i,j]
a=[list(input()) for i in range(h)]
q=int(input())
for i in range(q):
	x,y=map(int,input().split())
	cumsum[0][0][0]+=x-1
	cumsum[0][0][1]+=y-1
	cumsum[x][0][0]+=h
	cumsum[0][y][1]+=w
for i in range(h):
	for j in range(w-1):
		cumsum[i][j+1][1] += cumsum[i][j][1]-2*q
for i in range(w):
	for j in range(h-1):
		cumsum[j+1][i][0] += cumsum[j][i][0]-2*q
for i in range(h):
	for j in range(w-1):	
		cumsum[i][j+1][0] = cumsum[i][j][0]
for i in range(w):
	for j in range(h-1):
		cumsum[j+1][i][1] = cumsum[j][i][1]
print(cumsum)
for i in range(h):
	ans=[]
	for j in range(w):
		ans.append(a[i+cumsum[i][j][0]][j+cumsum[i][j][1]])
	print(''.join(ans))