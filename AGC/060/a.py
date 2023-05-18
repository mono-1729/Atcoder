n=int(input())
s=list(input())
sl=[ord(i)-ord('a') if i!='?' else 26 for i in s]
dp=[[[0]*27 for i in range(27)] for j in range(n+1)]
dp[0][26][26]=1
mod=998244353
for i in range(n):
  for j in range(26):
    for k in range(27):
      for l in range(27):
        if j==sl[i] or sl[i]==26:
          if j!=k and j!=l:
            dp[i+1][k][j]+=dp[i][l][k]
            dp[i+1][k][j]%=mod
print(sum(dp[n][i][j] for i in range(26) for j in range(26))%mod)