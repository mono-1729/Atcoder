from bisect import bisect
n,t=map(int,input().split())
a=list(map(int,input().split()))
ans=0
time=[0]
a_left=a[:20]
a_right=a[20:]
for i in range(1<<len(a_right)):
	num=0
	for j in range(len(a_right)):
		if i>>j &1:
			num+=a_right[j]
	time.append(num)
time.sort()
for i in range(1<<len(a_left)):
	num=0
	for j in range(len(a_left)):
		if i>>j &1:
			num+=a_left[j]
	if num<=t:
		ans=max(ans,num+time[bisect(time,t-num)-1])
print(ans)
