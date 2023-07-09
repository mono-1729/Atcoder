t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    x=n
    num=n-k
    if num%2==1:
        print('No')
        continue
    while True:
        if num<=(x//3)*2:
            print('Yes')
            break
        if x<3:
            print('No')
            break
        num-=(x//3)*2
        x//=3
        