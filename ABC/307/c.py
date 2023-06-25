ha,wa=map(int,input().split())
a=[list(input()) for _ in range(ha)]
hb,wb=map(int,input().split())
b=[list(input()) for _ in range(hb)]
hx,wx=map(int,input().split())
x=[list(input()) for _ in range(hx)]
ac=0
bc=0
for i in range(ha):
	for j in range(wa):
		if a[i][j]=='#':
			ac+=1
for i in range(hb):
	for j in range(wb):
		if b[i][j]=='#':
			bc+=1
for i in range(-hx,hx):
	for i2 in range(-wx,wx):
		for j in range(-hx,hx):
			for j2 in range(-wx,wx):
				flg=True
				acount=0
				bcount=0
				for h in range(hx):
					for w in range(wx):
						if x[h][w]=='#':
							ff=True
							if 0<=i+h<ha and 0<=i2+w<wa:
								if a[i+h][i2+w]=='#':
									acount+=1
									ff=False
							if 0<=j+h<hb and 0<=j2+w<wb:
								if b[j+h][j2+w]=='#':
									bcount+=1
									ff=False
							if ff:
								flg=False
								break
						else:
							if 0<=i+h<ha and 0<=i2+w<wa:
								if a[i+h][i2+w]=='#':
									flg=False
									break
							if 0<=j+h<hb and 0<=j2+w<wb:
								if b[j+h][j2+w]=='#':
									flg=False
									break
				if flg and acount==ac and bcount==bc:
					print('Yes')
					exit()
print('No')