n=int(input())
c=[0]*7
for i in range(7):
    for j in reversed(range(n+2)):
        if j*(j-1)//2<=n:
            c[i]=j
            n-=j*(j-1)//2
            break
c[0]-=1
ans=[]
mod=0
digit=1
for i in range(7):
	for _ in range(c[i]):
		for j in range(1,8):
			if (mod+digit*j)%7==i:
				ans.append(j)
				mod=i
				break
		digit=(digit*10)%7
print(''.join(map(str,reversed(ans))))