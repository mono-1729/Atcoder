h,w=map(int,input().split())
s=[list(input()) for _ in range(h)]
for i in range(h):
	for j in range(w-4):
		if s[i][j]=='s' and s[i][j+1]=='n' and s[i][j+2]=='u' and s[i][j+3]=='k' and s[i][j+4]=='e':
			for k in range(5):
				print(i+1,j+k+1)
			exit()
for i in range(h):
	for j in reversed(range(4,w)):
		if s[i][j]=='s' and s[i][j-1]=='n' and s[i][j-2]=='u' and s[i][j-3]=='k' and s[i][j-4]=='e':
			for k in range(5):
				print(i+1,j-k+1)
			exit()
for i in range(h-4):
	for j in range(w):
		if s[i][j]=='s' and s[i+1][j]=='n' and s[i+2][j]=='u' and s[i+3][j]=='k' and s[i+4][j]=='e':
			for k in range(5):
				print(i+k+1,j+1)
			exit()
for i in reversed(range(4,h)):
	for j in range(w):
		if s[i][j]=='s' and s[i-1][j]=='n' and s[i-2][j]=='u' and s[i-3][j]=='k' and s[i-4][j]=='e':
			for k in range(5):
				print(i-k+1,j+1)
			exit()
for i in range(h-4):
	for j in range(w-4):
		if s[i][j]=='s' and s[i+1][j+1]=='n' and s[i+2][j+2]=='u' and s[i+3][j+3]=='k' and s[i+4][j+4]=='e':
			for k in range(5):
				print(i+k+1,j+k+1)
			exit()
for i in reversed(range(4,h)):
	for j in reversed(range(4,w)):
		if s[i][j]=='s' and s[i-1][j-1]=='n' and s[i-2][j-2]=='u' and s[i-3][j-3]=='k' and s[i-4][j-4]=='e':
			for k in range(5):
				print(i-k+1,j-k+1)
			exit()
for i in range(h-4):
	for j in reversed(range(4,w)):
		if s[i][j]=='s' and s[i+1][j-1]=='n' and s[i+2][j-2]=='u' and s[i+3][j-3]=='k' and s[i+4][j-4]=='e':
			for k in range(5):
				print(i+k+1,j-k+1)
			exit()
for i in reversed(range(4,h)):
	for j in range(w-4):
		if s[i][j]=='s' and s[i-1][j+1]=='n' and s[i-2][j+2]=='u' and s[i-3][j+3]=='k' and s[i-4][j+4]=='e':
			for k in range(5):
				print(i-k+1,j+k+1)
			exit()