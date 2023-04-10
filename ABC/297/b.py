s=input()
b=[]
for i in range(8):
    if s[i]=='B':
        b.append(i)
if b[0]%2==b[1]%2:
    print('No')
    exit()
k=[]
q=0
for i in range(8):
    if s[i]=='R':
        k.append(i)
    if s[i]=='K':
        q=i
if not(k[0]<=q<=k[1]):
    print('No')
    exit()
print('Yes')