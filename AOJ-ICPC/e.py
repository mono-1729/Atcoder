n=int(input())
yx=[]
for i in range(n):
    x,y=map(int,input().split())
    yx.append((y,x))
dp=[[[-1,-1] for i in range(2*n)] for j in range(n+1)]
dp[0][0]=[10**9,10**9]

