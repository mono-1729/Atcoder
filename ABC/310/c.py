n=int(input())
sset=set()
for i in range(n):
    s=list(input())
    sset.add(min(''.join(s),''.join(reversed(s))))
print(len(sset))