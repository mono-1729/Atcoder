s=input()
t=input()
left=[0]*(len(t)+1)
right=[0]*(len(t)+1)
left[0]=1
right[0]=1
for i in range(len(t)):
	if left[i]==1 and (s[i]==t[i] or s[i]=='?' or t[i]=='?'):
		left[i+1]=1
	if right[i]==1 and (s[-i-1]==t[-i-1] or s[-i-1]=='?' or t[-i-1]=='?'):
		right[i+1]=1
for i in range(len(t)+1):
	if left[i]==1 and right[len(t)-i]==1:
		print('Yes')
	else:
		print('No')