n,m=map(int,input().split())
par=[-1]*n
check=[False]*n
check[0]=True
pos=0
for i in range(2*n):
    v=list(map(int,input().split()))[1:]
    flg=True
    for vv in v:
        if check[vv-1]:
            continue
        print(vv)
        par[vv-1]=pos
        pos=vv-1
        check[vv-1]=True
        flg=False
        if vv==n:
            ok=input()
            exit()
        break
    if flg:
        pos=par[pos]
        print(pos+1)
        