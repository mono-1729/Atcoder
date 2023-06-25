n=int(input())
p=list(map(int,input().split()))
count=0
for i in range(n-1):
	for j in range(i+1,n):
		if p[i]>p[j]:
			count+=1
if count%2==1:
	print('No')
	exit()
print('Yes')
ans=[]
l=0
for i in range(2*10**3):
	for j in range(l,n-2):
		if p[j]==j+1 and l==j:
			l+=1
		if (p[j]>p[j+1] and p[j+1]>p[j+2]) or (p[j+1]>p[j] and p[j]>p[j+2]):
			ans.append([j+1,j+1])
			p[j],p[j+1],p[j+2]=p[j+2],p[j],p[j+1]
		if p[j]>p[j+2] and p[j+2]>p[j+1]:
			ans.append([j+2,j])
			p[j],p[j+1],p[j+2]=p[j+1],p[j+2],p[j]
		if p[j+1]
print(len(ans))
for i in ans:
	print(*i)