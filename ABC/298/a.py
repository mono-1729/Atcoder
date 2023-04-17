n=int(input())
s=input()
flag=False
for i in range(n):
    if s[i]=='x':
        print('No')
        exit()
    if s[i]=='o':
        flag=True
if flag:
    print('Yes')
else:
    print('No')