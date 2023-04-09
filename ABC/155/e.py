n=list(input())
num=0
ans=0
for i in reversed(range(len(n))):
    money=int(n[i])+num
    if money>=6 or (money==5 and i>0 and int(n[i-1])>=5):
        ans+=10-money
        num=1
    else:
        ans+=money
        num=0
ans+=num
print(ans)