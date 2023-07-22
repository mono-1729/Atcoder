n=int(input())
s=list(input())
x=set()
for i in range(n):
    x.add(s[i])
    if len(x)==3:
        print(i+1)
        exit()
