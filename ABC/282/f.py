N = int(input())

ks = []
w = 1
while w <= 2048:
    for l in range(1,N+1):
        r = l+w-1
        if r > N: break
        ks.append((l,r))
    w *= 2

ks.sort()
print(len(ks))
for l,r in ks:
    print(l,r)

Q = int(input())
from bisect import bisect
for _ in range(Q):
    L,R = map(int,input().split())
    w = R-L+1
    k = len(bin(w))-3
    a = bisect(ks, (L,L+2**k-1))
    b = bisect(ks, (R-(2**k-1),R))
    print(a,b)