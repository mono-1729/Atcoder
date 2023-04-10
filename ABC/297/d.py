a,b=map(int,input().split())
count=0
while True:
    if a==b:
        print(count)
        exit()
    if a<b:
        a,b=b,a
    if a%b==0:
        print(count+(a-b)//b)
        exit()
    num=a-b
    cc=1+num//b
    a-=b*cc
    count+=cc
    