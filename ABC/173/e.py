n,k=map(int,input().split())
a=list(map(int,input().split()))
mod=10**9+7
ans=1
plus=[]
minus=[]
for i in a:
	if i>=0:
		plus.append(i)
	else:
		minus.append(i)
plus.sort()
minus.sort(reverse=True)
count=0
if len(plus)<max(1,k-(len(minus)//2)*2) and k%2:
	b=[(abs(a[i]),a[i])	for i in range(n)]
	b.sort()
	for i in range(k):
		ans*=b[i][1]
		ans%=mod
	print(ans)
	exit()
while k>0:
	if k%2==1:
		ans*=plus.pop()
		ans%=mod
		k-=1
		continue
	if len(plus)>=2 and len(minus)>=2:
		if plus[-1]*plus[-2]>minus[-1]*minus[-2]:
			ans*=plus.pop()
			ans*=plus.pop()
			ans%=mod
		else:
			ans*=minus.pop()
			ans*=minus.pop()
			ans%=mod
	elif len(plus)>=2:
		ans*=plus.pop()
		ans*=plus.pop()
		ans%=mod
	elif len(minus)>=2:
		ans*=minus.pop()
		ans*=minus.pop()
		ans%=mod
	else:
		ans*=plus.pop()
		ans*=minus.pop()
		ans%=mod
	k-=2
print(ans)