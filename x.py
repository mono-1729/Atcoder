r,c=map(int,input().split())
n=int(input())
rlist=set([0,r])
clist=set([0,c])
node_list=[]
for i in range(n):
	a,b,q,d=map(int,input().split())
	rlist.add(a)
	rlist.add(q)
	clist.add(b)
	clist.add(d)
	node_list.append([a,b,q,d])
rlist=list(rlist)
rlist.sort()
clist=list(clist)
clist.sort()
ans=0
x=[0.5,0]
y=[0.5,0]
while x[0]<r:
	y=[0.5,0]
	while y[0]<c:
		lx=[0,int(x[0]+0.5)]
		ly=[0,int(y[0]+0.5)]
		for n1,n2,n3,n4 in node_list:
			if n1<=x[0] and x[0]<=n3:
				ly[0]=max(n2,ly[0]) if y[0]>n2 else ly[0]
			if n2<=y[0] and y[0]<=n4:
				lx[0]=max(n1,lx[0]) if x[0]>n1 else lx[0]
		lx_y=ly
		ly_x=lx
		for n1,n2,n3,n4 in node_list:
			if (lx[0]<n1 and n1<lx[1]) or (lx[0]<n3 and n3<lx[1]):
				lx_y[0]=max(n4,lx_y[0]) if y[0]>n4 else lx_y[0]
				lx_y[1]=min(n2,lx_y[1]) if y[0]<n2 else lx_y[1]
			if (ly[0]<n2 and n2<ly[1]) or (ly[0]<n4 and n4<ly[1]):
				ly_x[0]=max(n3,ly_x[0]) if x[0]>n3 else ly_x[0]
				ly_x[1]=min(n1,ly_x[1]) if x[0]<n1 else ly_x[1]
		ans=max(ans,(lx[1]-lx[0])*(lx_y[1]-lx_y[0]))
		ans=max(ans,(ly[1]-ly[0])*(ly_x[1]-ly_x[0]))
		lx=[int(x[0]-0.5),r]
		ly=[int(y[0]-0.5),c]
		for n1,n2,n3,n4 in node_list:
			if n1<=x[0] and x[0]<=n3:
				ly[1]=min(n2,ly[1]) if y[0]<n2 else ly[1]
			if n2<=y[0] and y[0]<=n4:
				lx[1]=min(n1,lx[1]) if x[0]<n1 else lx[1]
		lx_y=ly
		ly_x=lx
		for n1,n2,n3,n4 in node_list:
			if (lx[0]<n1 and n1<lx[1]) or (lx[0]<n3 and n3<lx[1]):
				lx_y[0]=max(n4,lx_y[0]) if y[0]>n4 else lx_y[0]
				lx_y[1]=min(n2,lx_y[1]) if y[0]<n2 else lx_y[1]
			if (ly[0]<n2 and n2<ly[1]) or (ly[0]<n4 and n4<ly[1]):
				ly_x[0]=max(n3,ly_x[0]) if x[0]>n3 else ly_x[0]
				ly_x[1]=min(n1,ly_x[1]) if x[0]<n1 else ly_x[1]
		ans=max(ans,(lx[1]-lx[0])*(lx_y[1]-lx_y[0]))
		ans=max(ans,(ly[1]-ly[0])*(ly_x[1]-ly_x[0]))
		print(x[0],y[0],lx,ly,lx_y,ly_x,ans)
		y[1]+=1
		y[0]=clist[y[1]]+0.5
	x[1]+=1
	x[0]=rlist[x[1]]+0.5
print(ans)