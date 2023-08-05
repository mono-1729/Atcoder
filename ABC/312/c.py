from bisect import bisect_left,bisect_right
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort()
b.sort()
def is_ok(num):
  return (bisect_right(a,num)>=m-bisect_left(b,num))
def meguru_bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2 
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok
print(meguru_bisect(-1,10**9+1))