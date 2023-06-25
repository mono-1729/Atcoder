n=int(input())
s=[list(input()) for _ in range(n)]
ans='No'
for i in range(n):
	for j in range(n):
		if i==j:
			continue
		ss=s[i]+s[j]
		flg=True
		for k in range(len(ss)):
			if ss[k]!=ss[-k-1]:
				flg=False
				break
		if flg:
			ans='Yes'
			break
print(ans)