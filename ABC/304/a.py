n=int(input())
sa=[list(input().split()) for i in range(n)]
m=10**9
mind=0
for i in range(n):
	if m>int(sa[i][1]):
		m=int(sa[i][1])
		mind=i
for i in range(n):
	print(sa[(mind+i)%n][0])