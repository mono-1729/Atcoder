n,m=map(int,input().split())
a=list(map(int,input().split()))
count=m
nums1=[0]
nums2=[0]
ans=10**18
if a[0]>a[1]:
	aa=a[2:]
	aa.sort()
	for i in range(len(aa)-m+1):
		x=10**9
		if a[0]<=aa[i]<=a[1] or a[0]<=a[i+count-1]<=a[1]:
			x=0
		else:
			if a[0]>aa[i]:
				x=min(x,a[0]-aa[i])
			else:
				x=min(x,aa[i]-a[1])
			if a[0]>aa[i+count-1]:
				x=min(x,a[0]-aa[i+count-1])
			else:
				x=min(x,aa[i+count-1]-a[1])
		ans=min(ans,aa[i+count-1]-aa[i]+a[0]-a[i]+x)
for i in range(2,n):
    if a[0]<=a[i]<=a[1]:
        count-=1
    else:
        if a[0]>a[i]:
            nums1.append(a[0]-a[i])
        else:
            nums2.append(a[i]-a[1])
nums1.sort()
nums2.sort()
if count<=0:
    print(0)
    exit()
for i in range(count+1):
    if i<len(nums1) and count-i<len(nums2):
    	ans=min(ans,nums1[i]+nums2[count-i])
print(ans)