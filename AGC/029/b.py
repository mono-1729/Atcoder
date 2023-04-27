from collections import defaultdict
n=int(input())
a=list(map(int,input().split()))
d=defaultdict(int)
a.sort(reverse=True)
ans=0
for i in range(n):
    d[a[i]]+=1
for x in a:
	if d[x]==0:
		continue
	num=pow(2,len(bin(x)[2:]))-x
	if num==x:
		if d[num]>=2:
			ans+=1
			d[num]-=2
	else:
		if d[num]>0:
			ans+=1
			d[x]-=1
			d[num]-=1
print(ans)
