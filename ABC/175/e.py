from sys import stdin
from collections import defaultdict
r,c,k=map(int,stdin.readline().split())
item=defaultdict(int)
for i in range(k):
	rr,cc,kk=map(int,stdin.readline().split())
	item[f'{rr-1},{cc-1}']=kk
dp=[[[0]*4 for i in range(c)] for j in range(r)]
dp[0][0][1]=item['0,0']
for i in range(r):
	for j in range(c):
		for x in range(4):
			if i>0:
				dp[i][j][0]=max(dp[i][j][0],dp[i-1][j][x])
				if item[f'{i},{j}']>0:
					dp[i][j][1]=max(dp[i][j][1],dp[i-1][j][x]+item[f'{i},{j}'])
			if j>0:
				dp[i][j][x]=max(dp[i][j][x],dp[i][j-1][x])
				if x>0 and item[f'{i},{j}']>0:
					dp[i][j][x]=max(dp[i][j][x],dp[i][j-1][x-1]+item[f'{i},{j}'])

print(max(dp[r-1][c-1]))