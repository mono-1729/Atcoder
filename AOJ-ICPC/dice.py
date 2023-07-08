d=[[2,3,5,4],[4,6,3,1],[6,5,1,2],[5,6,2,1],[6,4,1,3],[4,5,3,2]]
while True:
	n=int(input())
	if n==0:
		exit()
	num=[[[0]*30 for _ in range(30)] for _ in range(50)]
	num[0]=[[-1]*30 for _ in range(30)]
	for  i in range(n):
		t,f=map(int,input().split())
		b=7-f
		r=-1
		l=-1
		x,y=15,15
		for j in range(4):
			if d[t-1][j]==f:
				r=d[t-1][(j+1)%4]
		l=7-r
		for j in reversed(range(50)):
			if num[j][x][y]==0:
				continue
			g=0
			new_f=0
			trans=(0,0)
			if f>=4:
				if num[j][x+1][y]==0 and g<f:
					g=f
					new_f=t
					trans=(1,0)	
			else:
				if num[j][x-1][y]==0 and g<b:
					g=b
					new_f=7-t
					trans=(-1,0)
			if r>=4:
				if num[j][x][y+1]==0 and g<r:
					g=r
					new_f=f
					trans=(0,1)
			else:
				if num[j][x][y-1]==0 and g<l:
					g=l
					new_f=f
					trans=(0,-1)
			# if i==n-1:
			# 	print(t,f,r,l,g,j,x,y)
			if g>0:
				x,y=x+trans[0],y+trans[1]
				t=7-g
				f=new_f
				b=7-f
				for k in range(4):
					if d[t-1][k]==f:
						r=d[t-1][(k+1)%4]
				l=7-r
			else:
				num[j+1][x][y]=t
				break
	ans=[0]*6
	for j in range(30):
		for k in range(30):
			for i in reversed(range(50)):
				if num[i][j][k]>0:
					ans[num[i][j][k]-1]+=1
					# print(i,j,k,num[i][j][k])
					break
	print(' '.join(map(str,ans)))