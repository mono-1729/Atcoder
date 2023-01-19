n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
q=int(input())
xy=[]
for i in range(q):
	x,y=map(int,input().split())
	xy.append((x,y,i))
xy.sort()
ans=['No']*q
count=0
a_set=set()
b_set=set()
diff=set()
l=0
r=0
for i in range(n):
	a_len=len(a_set)
	if a[i] in a_set and len(diff)==0:
		while count<q and xy[count][0]<=i+1:
			if l<=xy[count][1]<=r and xy[count][0]==i+1:
				ans[xy[count][2]]='Yes'
			count+=1
	elif not a[i] in a_set:
		l=r+1
		a_set.add(a[i])
		if a[i] in diff:
			diff.remove(a[i])
		else:
			diff.add(a[i])
		while r<n and len(a_set)>=len(b_set):
			if b[r] in b_set:
				r+=1
				continue
			else:
				if len(a_set)>len(b_set):
					b_set.add(b[r])
					if b[r] in diff:
						diff.remove(b[r])
					else:
						diff.add(b[r])
					r+=1
				else:
					break
		# print(f'{i} {count} {list(diff)} {l} {r}')
		if len(diff)==0:
			while count<q and xy[count][0]<=i+1:
				if l<=xy[count][1]<=r and xy[count][0]==i+1:
					ans[xy[count][2]]='Yes'
				count+=1
# print(f'{i} {count} {list(diff)} {l} {r}')
for i in range(q):
	print(ans[i])
