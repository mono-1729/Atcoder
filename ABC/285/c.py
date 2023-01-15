s=input()
ans=0
for i in range(len(s)):
	ans+=(ord(s[-1-i])-ord('A')+1)*26**i
print(ans)