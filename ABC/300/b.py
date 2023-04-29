h,w=map(int,input().split())
a=[input() for _ in range(h)]
b=[input() for _ in range(h)]
for i in range(h):
	for j in range(w):
		flg=True
		for k in range(h):
			for l in range(w):
				if a[k][l]!=b[(k+i)%h][(l+j)%w]:
					flg=False
					break
		if flg:
			print('Yes')
			exit()
print('No')