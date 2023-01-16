h,w=map(int,input().split())
A=[list(input()) for i in range(h)]
q=int(input())
x=[0,1]
y=[0,1]
for i in range(q):
	a,b=map(int,input().split())
	for j in range(2):
		if x[j]<a:
			x[j]=a-x[j]-1
		else:
			x[j]=h+a-x[j]-1
	for j in range(2):
		if y[j]<b:
			y[j]=b-y[j]-1
		else:
			y[j]=w+b-y[j]-1
x[1]=1 if (x[0]+1)%h==x[1]%h else -1
y[1]=1 if (y[0]+1)%w==y[1]%w else -1
print(x)
print(y)
for i in range(h):
	ans=[]
	for j in range(w):
		ans.append(A[(-x[1]*x[0]+i*x[1])%h][(-y[1]*y[0]+j*y[1])%w])
	print(''.join(ans))