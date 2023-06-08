from itertools import *
n,m=map(int,input().split())
s=[list(input()) for i in range(n)]
nums=[i for i in range(n)]
p=permutations(nums,n)
for i in p:
	flag=True
	for j in range(n-1):
		num=0
		for k in range(m):
			if s[i[j]][k]!=s[i[j+1]][k]:
				num+=1
		if num>1:
			flag=False
			break
	if flag:
		print('Yes')
		exit()
print('No')
exit()
