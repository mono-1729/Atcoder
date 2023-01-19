n,k=map(int,input().split())
a=list(map(int,input().split()))
ans=0
bin_k=bin(k)[2:].zfill(40)
digit_num=[[0,0] for i in range(40)]
for i in range(40):
	num0=0
	num1=0
	for j in range(n):
		if a[j]>>i & 1:
			num0+=1
		else:
			num1+=1
	digit_num[i]=[num0<<i,num1<<i]
for i in range(40):
	ans+=digit_num[i][int(bin_k[-1-i])]
for i in range(40):
	if 1<<i > k:
		break
	if not (k>>i & 1):
		continue
	num=0
	for j in range(i):
		num+=max(digit_num[j])
	num+=digit_num[i][0]
	for j in range(i+1,40):
		num+=digit_num[j][int(bin_k[-1-j])]
	ans=max(num,ans)
print(ans)