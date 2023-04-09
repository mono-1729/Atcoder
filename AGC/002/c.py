n,l=map(int,input().split())
a=list(map(int,input().split()))
num=0
for i in range(n-1):
    if a[i]+a[i+1]>=l:
        num=i+1
if num==0:
    print('Impossible')
else:
    print('Possible')
    for i in reversed(range(num+1,n)):
        print(i)
    for i in range(1,num):
        print(i)
    print(num)