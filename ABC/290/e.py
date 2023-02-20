n=int(input())
a=list(map(int,input().split()))
num=[[] for i in range(n+1)]
for i in range(n):
    num[a[i]].append(i)
ans=0
if n%2==0:
    ans=(n*(n+2)*(2*n-1))//24
else:
    ans=((n-1)*(n+1)*(2*n+3))//24
for i in range(1,n+1):
	if num[i]!=[]:
		x=0
		count=0
		mi=0
		ma=len(num[i])-1
		for j in range(len(num[i])):
			if num[i][mi]+1<=n-num[i][ma]:
				x+=count
				count+=num[i][mi]+1
				mi+=1
			else:
				x+=count
				count+=n-num[i][ma]
				ma-=1
		ans-=x
print(ans)