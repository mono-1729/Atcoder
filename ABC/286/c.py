n,a,b=map(int,input().split())
s=input()
s=s+s
ans=10**20
for i in range(n):
    num=i*a
    for j in range(n//2):
        if s[i+j]!=s[i+n-j-1]:
            num+=b
    print(num)
    ans=min(ans,num)
print(ans)