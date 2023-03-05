s=input()
ans=[]
for i in len(s):
    ans.append(chr(ord(s[i])-32))
print(''.join(ans))