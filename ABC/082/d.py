s=list(input())
gx,gy=map(int,input().split())
x_act=[]
y_act=[]
start=0
num=0
count=0
f=0
while count<len(s) and s[count]=='F':
	count+=1
start=count
while count<len(s):
	if s[count]=='F':
		f+=1
	if s[count]=='T':
		if f>0:
			if num==0:
				x_act.append(f)
			else:
				y_act.append(f)
			f=0
		num=(num+1)%2
	count+=1
if f>0:
	if num==0:
		x_act.append(f)
	else:
		y_act.append(f)
# print(x_act,y_act)
xdist=abs(gx-start)
ydist=abs(gy)
dp=[[0]*8001 for i in range(len(x_act)+1)]
dp[0][0]=1
for i in range(len(x_act)):
	for j in range(8001):
		if dp[i][j]==1:
			dp[i+1][j+x_act[i]]=1
			dp[i+1][abs(j-x_act[i])]=1
if xdist>8000 or dp[len(x_act)][xdist]==0:
	print('No')
	exit()
dp=[[0]*8001 for i in range(len(y_act)+1)]
dp[0][0]=1
for i in range(len(y_act)):
	for j in range(8001):
		if dp[i][j]==1:
			dp[i+1][j+y_act[i]]=1
			dp[i+1][abs(j-y_act[i])]=1
if dp[len(y_act)][ydist]==0:
	print('No')
else:
	print('Yes')