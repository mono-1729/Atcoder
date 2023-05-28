n=int(input())
s=list(input())
t=list(input())
for i in range(n):
	if s[i]!=t[i]:
		if not (s[i] in {'1','l'} and t[i] in {'1','l'}):
			if not (s[i] in {'0','o'} and t[i] in {'0','o'}):
				print('No')
				exit()
print('Yes')
			