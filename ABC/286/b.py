n=int(input())
s=input()
ans=[]
i=0
while i<n:
	if i==n-1:
		ans.append(s[i])
		i+=1
		
	elif s[i]=='n' and s[i+1]=='a':
		ans.append('n')
		ans.append('y')
		ans.append('a')
		i+=2
		
	else:
		ans.append(s[i])
		i+=1
print("".join(ans))