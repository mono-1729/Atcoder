N = int(input())
xyz = []
for i in range(N):
    x,y,z = map(int,input().split())
    xyz.append((x,y,z))
    
dist = [[None]*N for i in range(N)]
for i in range(N):
    for j in range(N):
        dist[i][j] = abs(xyz[i][0]-xyz[j][0])+abs(xyz[i][1]-xyz[j][1])+max(0,xyz[j][2]-xyz[i][2])
        
all = 1<<N

dp = [[10**100]*N for i in range(all)]
dp[0][0] = 0

def check(n,j):
    return (n&(1<<j) > 0)

for n in range(all):
    for i in range(N):
        for j in range(N):
            if check(n,j) or i == j:
                continue
            dp[n|(1<<j)][j] = min(dp[n|(1<<j)][j],dp[n][i]+dist[i][j])
            
print(dp[all-1][0])