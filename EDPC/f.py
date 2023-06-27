s=input()
t=input()
dp=[0 for i in range(len(t)+1)]
dps=[dp.copy()]
for i in range(len(s)):
	ndp=[0 for i in range(len(t)+1)]
	for j in range(len(t)):
		if s[i]==t[j]:
			ndp[j+1]=max(ndp[j],dp[j+1],dp[j]+1)
		else:
			ndp[j+1]=max(ndp[j],dp[j+1])
	dp=ndp
	dps.append(dp.copy())
ans=[]
i=len(s)
j=len(t)
while dps[i][j]:
	if dps[i-1][j]==dps[i][j]:
		i-=1
	elif dps[i][j-1]==dps[i][j]:
		j-=1
	else:
		ans.append(s[i-1])
		i-=1
		j-=1
print(''.join(reversed(ans)))
#print(dps)