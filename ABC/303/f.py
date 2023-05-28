n,h=map(int,input().split())
ju=[]
l=[]
bi=[]
for i in range(n):
   t,d=map(int,input().split())
   ju.append([t*d,d,t,i])

ju.sort(reverse=True)
pre=-1
for sum,d,t,i in ju:
	if pre==-1:
		l.append([d,t])
		pre=1
	else:
		if sum>l[-1][0]*min(l[-1][1],t):
			bi.append((l[-1][0]*l[-1][1])/l[-1][0])
			l.append([d,t])
def is_ok(arg):
	day=arg
	num=0
	for i in range(len(bi)):
		if bi[i]<=day:
			d,t=l[i]
			num+=(max(0,day-t+1))*d*t
			day=min(day,t-1)
			num+=((day-int(bi[i]))*((day+int(bi[i])+1)*d))//2
			day=int(bi[i])
	d,t=l[-1]
	num+=(max(0,day-t+1))*d*t
	day=min(day,t-1)
	num+=((day)*((day+1)*d))//2
	day=0
	return num>=h
def meguru_bisect(ng, ok):
	while (abs(ok - ng) > 1):
		mid = (ok + ng) // 2 
		if is_ok(mid):
			ok = mid
		else:
			ng = mid
	return ok
print(meguru_bisect(0,10**18+1))