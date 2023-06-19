p,q=input().split()
p=ord(p)-ord('A')
q=ord(q)-ord('A')
p,q=min(p,q),max(p,q)
l=[3,1,4,1,5,9]
ans=0
for i in range(p,q):
	ans+=l[i]
print(ans)