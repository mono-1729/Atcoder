n,m=map(int,input().split())
s=[list(input()) for i in range(n)]
for i in range(n-8):
    for j in range(m-8):
        flg=True
        for x in range(3):
            for y in range(3):
                if s[i+x][j+y]=='.':
                    flg=False
        for x in range(3):
            for y in range(3):
                if s[i+x+6][j+y+6]=='.':
                    flg=False
        for x in range(4):
            if s[i+3][j+x]=='#':
                flg=False
        for x in range(4):
            if s[i+5][j+x+5]=='#':
                flg=False
        for x in range(4):
            if s[i+x][j+3]=='#':
                flg=False
        for x in range(4):
            if s[i+x+5][j+5]=='#':
                flg=False
        if flg:
            print(i+1,j+1)