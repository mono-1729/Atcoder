n,m,h,k=map(int,input().split())
s=list(input())
p=set()
for i in range(m):
	x,y=map(int,input().split())
	p.add((x,y))
num=h
now=[0,0]
for i in range(n):
	if s[i]=='U':
		now[1]+=1
	elif s[i]=='D':
		now[1]-=1
	elif s[i]=='R':
		now[0]+=1
	elif s[i]=='L':
		now[0]-=1
	num-=1
	if num<0:
		print('No')
		exit()
	if (now[0],now[1]) in p and num<k:
		num=k
		p.remove((now[0],now[1]))
print('Yes')