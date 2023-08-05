n,m=map(int,input().split())
x1=[]
x2=[]
x3=[]
for i in range(n):
	t,x=map(int,input().split())
	if t==0:
		x1.append(x)
	if t==1:
		x2.append(x)
	if t==2:
		x3.append(x)
x1.sort(reverse=True)
x2.sort(reverse=True)
x3.sort(reverse=True)
ans=0
if len(x1)>0:
	ans=x1[min(len(x1)-1,m-1)]
num=ans
xx1=min(len(x1)-1,m-1)
xx2=0
xx3=0
count=min(len(x1)-1,m-1)
kan=0
for i in range(min(m,len(x3))):
	kan+=x3[0]
	
	ans=max(ans,num)
print(ans)