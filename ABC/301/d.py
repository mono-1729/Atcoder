s=list(input())
sl=len(s)
n=int(input())
num=0
for i in range(sl):
	if s[i]=='1':
		num+=pow(2,sl-i-1)
for i in range(sl):
	if s[i]=='?':
		if num+pow(2,sl-i-1)<=n:
			num+=pow(2,sl-i-1)
if num<=n:
	print(num)
else:
	print(-1)
        