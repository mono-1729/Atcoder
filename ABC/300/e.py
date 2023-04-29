n=int(input())
num=[0,0,0]
while n%2==0:
	num[0]+=1
	n//=2
while n%3==0:
	num[1]+=1
	n//=3
while n%5==0:
	num[2]+=1
	n//=5
if n!=1:
	print(0)
	exit()
dp=[[[0]*(num[2]+1) for _ in range(num[1]+1)] for _ in range(num[0]+1)]
dp[0][0][0]=1
mod=998244353
den=pow(5,mod-2,mod)
for i in range(num[0]+1):
	for j in range(num[1]+1):
		for k in range(num[2]+1):
			if i!=num[0]:
				dp[i+1][j][k]=(dp[i+1][j][k]+dp[i][j][k]*den)%mod
				if j!=num[1]:
					dp[i+1][j+1][k]=(dp[i+1][j+1][k]+dp[i][j][k]*den)%mod
				if i<num[0]-1:
					dp[i+2][j][k]=(dp[i+2][j][k]+dp[i][j][k]*den)%mod
			if k!=num[2]:
				dp[i][j][k+1]=(dp[i][j][k+1]+dp[i][j][k]*den)%mod
			if j!=num[1]:
				dp[i][j+1][k]=(dp[i][j+1][k]+dp[i][j][k]*den)%mod
print((dp[num[0]][num[1]][num[2]])%mod)