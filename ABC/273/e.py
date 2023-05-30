
from collections import defaultdict
from sys import stdin
p = [0]
v = [-1]
note = defaultdict(int)
now = 0

q = int(input())
ans = []
for _ in range(q):
    s = stdin.readline()
    
    if s[0] == "D":
        now = p[now]
    else:
        _, x = s.split()
        x = int(x)
    
    if s[0] == "A":
        p.append(now)
        v.append(x)
        now = len(p) - 1
    elif s[0] == "S":
        note[x] = now
    elif s[0] == "L":
        now = note[x]
    
    ans.append(v[now])

print(*ans)