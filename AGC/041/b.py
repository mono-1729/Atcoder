n,m,v,p=map(int,input().split())
a=list(map(int,input().split()))
a.sort(reverse=True)
ok=0
ng=n+1
def is_ok(num):
	if num<p:
		return True
	point=0
	score=a[num]+m
	for i in range(n):
		if i<p-1:
			point+=m
		elif score>a[i]:
			point+=min(m,score-a[i])
	if score>=a[p-1] and point>=m*v:
		return True
	else:
		return False
while (abs(ng - ok) > 1):
	mid = (ok + ng) // 2 
	if is_ok(mid-1):
		ok = mid
	else:
		ng = mid
print(ok)