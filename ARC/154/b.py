from collections import defaultdict
from bisect import bisect_right  
n=int(input())
s=input()
t=input()
ss=defaultdict(int)
tt=defaultdict(int)
ttt=defaultdict(list)
for i in range(n):
    ss[s[i]]+=1
    tt[t[i]]+=1
    ttt[t[i]].append(i)
for i in range(n):
    if ss[s[i]]!=tt[s[i]]:
           print(-1)
           exit()
ans=n
num=n-1
for i in reversed(range(n)):
	if ttt[s[i]]==[]:
		break
	nn=bisect_right(ttt[s[i]],num)
	if nn>0:
		ans-=1
		num=ttt[s[i]][nn-1]
		_=ttt[s[i]].pop(nn-1)
	else:
		break
print(ans)