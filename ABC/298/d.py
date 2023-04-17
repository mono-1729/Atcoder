q=int(input())
ans=1
count=0
s=[1]
am=[1]
for i in range(q):
    query=list(map(int,input().split()))
    if query[0]==1:
        _,i=query
        s.append(i)
        ans=(ans*10+i)%998244353
        am.append((am[-1]*10)%998244353)
    if query[0]==2:
        ans=(9982443530+ans-am[-1]*s[count])%998244353
        am.pop()
        count+=1
    if query[0]==3:
        print(ans)