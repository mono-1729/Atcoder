n=int(input())
s=input()
if (not'-' in s) or (not 'o' in s):
    print(-1)
    exit()
count=0
ans=0
for i in range(n):
    if s[i]=='o':
        count+=1
    else:
        count=0
    ans=max(ans,count)
print(ans)