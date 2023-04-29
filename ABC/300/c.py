h,w=map(int,input().split())
c=[list(input()) for _ in range(h)]
ans=[0]*min(h,w)
for i in range(h):
	for j in range(w):
		if c[i][j]=='#':
			num=0
			while i+num<h and j+num<w and c[i+num][j+num]=='#' :
				c[i+num][j+num]='.'
				num+=1
			for k in range(num):
				c[i+num-1-k][j+k]='.'
			ans[num//2-1]+=1
print(' '.join(list(map(str,ans))))