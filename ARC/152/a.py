n,l=map(int,input().split())
a=list(map(int,input().split()))
ch=[0]*l
num=0
count=0
for i in range(n):
	if a[i]+num<=l:
		num+=a[i]+1
	else:
		break
	count=i
for i in range(count+1,n):
	if a[i]==2:
		print('No')
		exit()
print('Yes')