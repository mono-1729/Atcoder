from itertools import *
n=int(input())
a=list(map(int,input().split()))
nn=[0 for i in range(4)]
num=[[0 for i in range(4)] for j in range(4)]
for i in range(n):
	nn[a[i]-1]+=1
for i in range(3):
	nn[i+1]+=nn[i]
for i in range(n):
	for j in range(4):
		if i+1<=nn[j]:
			num[a[i]-1][j]+=1
			break
p=permutations([0,1,2,3],4)
ans=0
for i in p:
	s=0
	for j in range(4):
		for k in range(j+1,4):
			s+=num[i[j]][i[k]]
	ans=max(ans,s)
print(ans)