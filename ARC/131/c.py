n=int(input())
a=list(map(int,input().split()))
num=0
for i in range(n):
	num^=a[i]
for i in range(n):
	if num==a[i]:
		print('Win')
		exit()
if n%2==1:
	print('Win')
else:
	print('Lose')