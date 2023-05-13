n=int(input())
a=list(map(int,input().split()))
ans=[a[0]]
for i in range(n-1):
	if a[i]>a[i+1]:
		for j in range(a[i]-a[i+1]-1):
			ans.append(a[i]-j-1)
	else:
		for j in range(a[i+1]-a[i]-1):
			ans.append(a[i]+j+1)
	ans.append(a[i+1])
print(' '.join(map(str,ans)))