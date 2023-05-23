n,m=map(int,input().split())
q=int(input())
mod=998244353
for i in range(q):
	a,b,c,d=map(int,input().split())
	ans=0
	if (b-a+1)%2==1:
		if (d-c+1)%2==1:
			if (b+d)%2==0:
				ans+=((d-c+1)//2+1)*(((2*b-2)*m+c+d)//2)
			else:
				ans+=((d-c+1)//2)*(((2*b-2)*m+c+d)//2)
		else:
			if (b+d)%2==0:
				ans+=((d-c+1)//2)*(((2*b-2)*m+c+d+1)//2)
			else:
				ans+=((d-c+1)//2)*(((2*b-2)*m+c+d-1)//2)
		b-=1
	#print(ans)
	if (d-c+1)%2==1:
		if (b+d)%2==0:
			ans+=((b-a+1)//2)*(((a+b-1)*m+2*d)//2)
		else:
			ans+=((b-a+1)//2)*(((a+b-3)*m+2*d)//2)
		d-=1
	#print(ans)
	ans+=((b-a+1)*(d-c+1)*((a+b-2)*m+c+d)//4)%mod
	print(ans%mod)
	#print('----ここまで----')