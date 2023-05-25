from functools import lru_cache
n,x=map(int,input().split())
a=list(map(int,input().split()))
@lru_cache(maxsize=None)
def solve(i,x):
    global a
    if i==len(a)-1:
        return x//a[i]
    return min(solve(i+1,x-x%a[i+1])+(x%a[i+1])//a[i],solve(i+1,x-x%a[i+1]+a[i+1])+(a[i+1]-x%a[i+1])//a[i])

print(solve(0,x))