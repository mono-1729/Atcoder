s=list(input())
for i in range(len(s)-1):
    if s[i]!=s[-i-2+len(s)]:
        print(-1)
        exit()
if s[0]=='0' or s[-1]=='1':
	print(-1)
	exit()
now=len(s)-1
for i in reversed(range(len(s)-1)):
    print(i+1,now+1)
    if s[i]=='1':
        now=i