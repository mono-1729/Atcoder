n=int(input())
a=list(map(int,input().split()))
print(2*n-2)
if max(a)> abs(min(a)):		
	print(a.index(max(a))+1,2)
	print(a.index(max(a))+1,2)
	for i in range(2,n):
		print(i,i+1)
		print(i,i+1)
else:
	print(a.index(min(a))+1,n-1)
	print(a.index(min(a))+1,n-1)
	for i in reversed(range(2,n)):
		print(i,i-1)
		print(i,i-1)