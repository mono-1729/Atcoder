h,w=map(int,input().split())
s=[list(input()) for _ in range(h)]
for i in range(h):
	for j in range(w):
		if s[i][j]=='#':
			continue
		count=0
		if i>0 and s[i-1][j]=='#':
			count+=1
		if i<h-1 and s[i+1][j]=='#':
			count+=1
		if j>0 and s[i][j-1]=='#':
			count+=1
		if j<w-1 and s[i][j+1]=='#':
			count+=1
		if count>=2:
			print(i+1,j+1)
			exit()