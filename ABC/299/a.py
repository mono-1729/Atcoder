n=int(input())
s=input()
flg=0
for i in range(n):
    if s[i]=='|':
        if flg==0:
            flg=1
        else:
            flg=0
    if s[i]=='*':
        if flg==1:
            print('in')
        else:
            print('out')