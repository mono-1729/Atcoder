n,m=map(int,input().split())
s=[input() for i in range(n)]
t=set([input() for i in range(m)])
count=0
for i in range(n):
    if s[i][3:] in t:
        count+=1
print(count)