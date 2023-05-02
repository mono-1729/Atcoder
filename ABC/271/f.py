from bisect import bisect_left,bisect_right
n=int(input())
nums=[[] for _ in range(n)]
a=[list(map(int,input().split())) for i in range(n)]
for i in range(2**(n-1)):
	count=a[0][0]
	pos=[0,0]
	for j in range(n-1):
		if (i>>j)&1:
			pos[0]+=1
			count^=a[pos[0]][pos[1]]
		else:
			pos[1]+=1
			count^=a[pos[0]][pos[1]]
	nums[pos[0]].append(count)
for i in range(n):
	nums[i].sort()
ans=0
for i in range(2**(n-1)):
	count=a[n-1][n-1]
	pos=[n-1,n-1]
	for j in range(n-1):
		if (i>>j)&1:
			pos[0]-=1
			count^=a[pos[0]][pos[1]]
		else:
			pos[1]-=1
			count^=a[pos[0]][pos[1]]
	count^=a[pos[0]][pos[1]]
	ans+=bisect_right(nums[pos[0]],count)-bisect_left(nums[pos[0]],count)
print(ans)
