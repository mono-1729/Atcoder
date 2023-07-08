import heapq
t=int(input())
nums={}
num=set([2,3,6])
nums[3]=[2,3,6]
for i in range(3,500):
	nnum=sorted(list(num.copy()))
	for j in nnum:
		for k in range(1,int(j**0.5)+1):
			if j%k==0:
				if j>=2 and j*(k+1) not in num and (j//k)*(k+1) not in num:
					num.remove(j)
					num.add(j*(k+1))
					num.add((j//k)*(k+1))
					break
				if (j//k)>=2 and j*((j//k)+1) not in num and (j//(j//k))*((j//k)+1) not in num:
					num.remove(j)
					num.add(j*(j//k+1))
					num.add((j//(j//k))*((j//k)+1))
					break
	nums[i+1]=list(num)
print(' '.join(map(str,list(num))))

for _ in range(t):
	n=int(input())
	if n==2:
		print('No')
		continue
	else:
		print('Yes')
	if n==1:
		print(1)
	else:
		print(' '.join(map(str,nums[n])))