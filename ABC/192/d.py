x=list(input())
m=int(input())
d=max(map(int,x))

ok=d+1
ng=m+1
def is_ok(num):
	s=0
	for i in range(len(x)):
		s+=pow(num,i)*int(x[-1-i])
		if s>m:
			return 0
	return 1
while (abs(ng - ok) > 1):
	mid = (ok + ng) // 2 
	if is_ok(mid):
		ok = mid
	else:
		ng = mid
if ok==d+1:
	if not is_ok(d+1):
		ok-=1
if len(x)==1:
	if ok-d:
		print(1)
		exit()
print(ok-d)