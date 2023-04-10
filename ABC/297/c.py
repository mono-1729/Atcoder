h,w=map(int,input().split())
s=[list(input())for i in range(h)]
count=0
for i in range(h): 
    for j in range(w-1):
        if s[i][j]=='T'and s[i][j+1]=='T':
            s[i][j]='P'
            s[i][j+1]='C'
for i in range(h):
    print(''.join(s[i]))