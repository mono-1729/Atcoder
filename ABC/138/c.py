n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    a[i]=(a[i],i)
b=sorted(a,reverse=True)
selected=[0]*n
ans=0
for i in range(n//2):
	ans+=b[i][0]
	selected[b[i][1]]=1
num=[0]
for s in selected:
    num.append(num[-1]-2*s+1)
print(num.index(min(num))%n,ans)