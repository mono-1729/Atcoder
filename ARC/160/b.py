t=int(input())
mod=998244353
for _ in range(t):
	#print('koko')
	n=int(input())
	num=[0]
	num2=0
	num3=[0]
	for i in range(1,n+1):
		if i**2>n:
			break
		num.append(n//i)
		num2+=n//i-i
		num3.append(num3[-1]+n//i-i)
	ans=0
	ans+=int(n**0.5)
	#ans%=mod
	#print(ans)
	for i in range(1,int(n**0.5)+1):
		if i**2>n:
			break
		ans+=(num[i]-1)*3
		ans%=mod
		#print(ans)
	for i in range(1,int(n**0.5)+1):
		if i**2>n:
			break
		ans+=(num2-num3[i])*6
		ans%=mod
		#print(ans)
	# print(num)
	#print(num2)
	print(ans)