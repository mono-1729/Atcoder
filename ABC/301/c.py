from collections import defaultdict
s=list(input())
t=list(input())
ss=defaultdict(int)
tt=defaultdict(int)
stset=set(s+t)
snum=0
tnum=0
sa=0
ta=0
at=set(['a','t','c','o','d','e','r'])
if len(s)!=len(t):
	print('No')
	exit()
for i in range(len(s)):
	ss[s[i]]+=1
	tt[t[i]]+=1
	if s[i]=='@':
		sa+=1
	if t[i]=='@':
		ta+=1
for i in stset:
	if ss[i]<tt[i]:
		if i in at:
			snum+=tt[i]-ss[i]
		elif i=='@':
			continue
		else:
			print('No')
			exit()
	elif ss[i]>tt[i]:
		if i in at:
			tnum+=ss[i]-tt[i]
		elif i=='@':
			continue
		else:
			print('No')
			exit()
if sa>=snum and ta>=tnum:
	print('Yes')
else:
	print('No')