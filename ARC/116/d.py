mod = 998244353
 
n, m = map(int,input().split())
nn = 5005
f = [1] * nn
inv = [1] * nn
for i in range(1, nn):
    f[i] = f[i-1] * i % mod
    inv[i] = pow(f[i], mod-2, mod)
 
 
def comb(n, k):
    if k < 0 or k > n:
        return 0
    return f[n] * inv[n-k] % mod * inv[k] % mod
 
 
dp = [0] * (m+1)
dp[0] = 1
for b in range(14):
    t = [0] * (m+1)
    for j in range(0, m+1, 2):
        val = (1 << b) * j
        for i in range(m+1):
            if i + val > m:
                break
            t[i+val] += dp[i] * comb(n, j) % mod
            t[i+val] %= mod
    dp = t
    # print(dp)
 
print(dp[m])
