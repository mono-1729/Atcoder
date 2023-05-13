n=int(input())
s=list(input())
t=0
a=0
for i in range(n):
    if s[i]=='T':
        t+=1
    else:
        a+=1
if t>a:
    print('T')
elif a>t:
	print('A')
else:
	if s[-1]=='T':
		print('A')
	else:
		print('T')