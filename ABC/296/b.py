s=[list(input())for i in range(8)]
ss=['a','b','c','d','e','f','g','h']
for i in range(8):
    for j in range(8):
        if s[i][j]=='*':
            print(f'{ss[j]}{8-i}')