n,k=map(int,input().split())
s=[input() for i in range(n)]
ss=s[:k]
ss.sort()
for i in range(k):
    print(ss[i])