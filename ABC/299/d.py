n=int(input())
s=[None]*n
def meguru_bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2 
        print(f'? {mid}')
        ss=int(input())
        if not ss:
            ng = mid
        else:
            ok = mid
    return ng
print(f'! {meguru_bisect(1,n)}')