s=list(map(int,input().split()))
for i in range(7):
    if s[i]>s[i+1]:
        print('No')
        exit()
        
for i in range(8):
    if s[i]%25!=0:
        print('No')
        exit()
    if s[i]<100 or s[i]>675:
        print('No')
        exit()
print('Yes')