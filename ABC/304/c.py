import sys
sys.setrecursionlimit(3*10**5)
n,d=map(int,input().split())
xy=[list(map(int,input().split())) for i in range(n)]
infect=['No']*n
infect[0]='Yes'
edge=[[] for i in range(n)]
for i in range(n):
	for j in range(1,n):
		if (abs(xy[i][0]-xy[j][0])**2+abs(xy[i][1]-xy[j][1])**2)<=d**2:
			edge[i].append(j)
			edge[j].append(i)
def infecter(pos):
	for i in edge[pos]:
		if infect[i]=='No':
			infect[i]='Yes'
			infecter(i)
infecter(0)
for i in range(n):
	print(infect[i])