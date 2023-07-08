n=int(input())
a=list(map(int,input().split()))
s=list(input())
num=[[0]*3,[0]*6]
ans=0
for i in range(n):
    if s[i]=='M':
        num[0][a[i]]+=1
    if s[i]=='E':
        for j in range(3):
            if j==a[i]:
                num[1][a[i]]+=num[0][j]
            else:
                num[1][6-a[i]-j]+=num[0][j]
    if s[i]=='X':
        for j in range(3):
            nn=[1,1,1]
            nn[j]=0
            nn[a[i]]=0
            for k in range(3):
                if nn[k]!=0:
                    ans+=num[1][j]*k
                    break
        for j in range(3,6):
            if j%3==a[i]:
                ans+=3*num[1][j]
            else:
                ans+=(j-3)*num[1][j]
print(ans)
