t=int(input())
for _ in range(t):
    n=int(input())
    s=list(input())
    flg=False
    check=False
    for i in range(1,n):
        if s[:i]<s[i:]:
            flg=True
            break
    if flg:
        print('Yes')
    else:
        print('No')