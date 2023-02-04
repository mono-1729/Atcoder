n=int(input())
s=[]
for i in range(n):
	ss=input()
	s.append((ss,i))
s.sort()
ans=[0]*n
for i in range(n):
	s1,num=s[i]
	count=0
	nn=0
	if i>0:
		s2,_=s[i-1]
		for j in range(min(len(s1),len(s2))):
			if s1[j]==s2[j]:
				nn+=1
			else:
				break
	count=max(count,nn)
	nn=0
	if i<n-1:
		s2,_=s[i+1]
		for j in range(min(len(s1),len(s2))):
			if s1[j]==s2[j]:
				nn+=1
			else:
				break
	count=max(count,nn)
	ans[num]=count
for i in range(n):
	print(ans[i])