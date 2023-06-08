t=int(input())
for _ in range(t):
	n,a,b,x,y,z=map(int,input().split())
	if a>b:
		a,b=b,a
		y,z=z,y
	p1=x
	p2=y/a
	p3=z/b
	if min(p1,p2,p3)==p1:
		print(n*x)
	elif min(p1,p2,p3)==p2:
		if p1<=p3:
			print(y*(n//a)+x*(n%a))
		else:
			ans=10**20
			for i in range(min(a+1,n//b+1)):
				ans=min(ans,z*i+y*((n-i*b)//a)+x*((n-i*b)%a))
			print(ans)
	else:
		if p1<=p2:
			print(z*(n//b)+x*(n%b))
		else:
			ans=10**20
			if b>n//b:
				for i in range(n//b+1):
					ans=min(ans,z*i+y*((n-i*b)//a)+x*((n-i*b)%a))
			else:
				for i in range(min(b+1,n//a+1)):
					ans=min(ans,y*i+z*((n-i*a)//b)+x*((n-i*a)%b))
			print(ans)