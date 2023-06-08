f = [1] * n
inv = [1] * n
for i in range(1, n):
    f[i] = f[i-1] * i % mod
    inv[i] = pow(f[i], mod-2, mod)
 
 
def comb(n, k):
    if k < 0 or k > n:
        return 0
    return f[n] * inv[n-k] % mod * inv[k] % mod