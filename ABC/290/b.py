n,k=map(int,input().split())
s=input()
ans=['x']*n
count=0
for i in range(n):
    if count<k and s[i]=='o':
        ans[i]='o'
        count+=1
print(''.join(ans))
        