n=int(input())
l=10**28
arg=[]
ans=0
for i in range(n):
    x,y=map(int,input().split())
    num=10**28 if x==1 else (y*(10**18))//(x-1)
    arg.append((((y-1)*(10**18))//x,num))
arg.sort(reverse=True)
for i in range(n):
	ar,al=arg[i]
	if al<=l:
		l=ar
		ans+=1
print(ans)
