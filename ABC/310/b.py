n,m=map(int,input().split())
pcf=[list(map(int,input().split())) for i in range(n)]
for i in range(n):
	for j in range(n):
		flg=True
		p1,c1,f1=pcf[i][0],pcf[i][1],set(pcf[i][2:])
		p2,c2,f2=pcf[j][0],pcf[j][1],set(pcf[j][2:])
		for k in f1:
			if k not in f2:
				flg=False
				break
		if flg and  p1>=p2 and (len(f1)<len(f2) or p1>p2):
			print('Yes')
			exit()
print('No')