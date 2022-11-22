# N: 処理する区間の長さ

INF = 2**31-1

LV = (N-1).bit_length()
N0 = 2**LV
data = [INF]*(2*N0)
lazy = [None]*(2*N0)
 
# 伝搬対象の区間を求める
def gindex(l, r):
    L = (l + N0) >> 1; R = (r + N0) >> 1
    lc = 0 if l & 1 else (L & -L).bit_length()
    rc = 0 if r & 1 else (R & -R).bit_length()
    for i in range(LV):
        if rc <= i:
            yield R
        if L < R and lc <= i:
            yield L
        L >>= 1; R >>= 1
 
# 遅延伝搬処理
def propagates(*ids):
    for i in reversed(ids):
        v = lazy[i-1]
        if v is None:
            continue
        lazy[2*i-1] = data[2*i-1] = lazy[2*i] = data[2*i] = v
        lazy[i-1] = None
 
# 区間[l, r)をxで更新
def update(l, r, x):
    *ids, = gindex(l, r)
    propagates(*ids)
 
    L = N0 + l; R = N0 + r
    while L < R:
        if R & 1:
            R -= 1
            lazy[R-1] = data[R-1] = x
        if L & 1:
            lazy[L-1] = data[L-1] = x
            L += 1
        L >>= 1; R >>= 1
    for i in ids:
        data[i-1] = min(data[2*i-1], data[2*i])
 
# 区間[l, r)内の最小値を求める
def query(l, r):
    propagates(*gindex(l, r))
    L = N0 + l; R = N0 + r
 
    s = INF
    while L < R:
        if R & 1:
            R -= 1
            s = min(s, data[R-1])
        if L & 1:
            s = min(s, data[L-1])
            L += 1
        L >>= 1; R >>= 1
    return s

# N: 処理する区間の長さ
LV = (N-1).bit_length()
N0 = 2**LV
data = [0]*(2*N0)
lazy = [None]*(2*N0)
 
def gindex(l, r):
    L = (l + N0) >> 1; R = (r + N0) >> 1
    lc = 0 if l & 1 else (L & -L).bit_length()
    rc = 0 if r & 1 else (R & -R).bit_length()
    for i in range(LV):
        if rc <= i:
            yield R
        if L < R and lc <= i:
            yield L
        L >>= 1; R >>= 1
 
# 遅延伝搬処理
def propagates(*ids):
    for i in reversed(ids):
        v = lazy[i-1]
        if v is None:
            continue
        lazy[2*i-1] = lazy[2*i] = data[2*i-1] = data[2*i] = v >> 1
        lazy[i-1] = None
 
# 区間[l, r)をxに更新
def update(l, r, x):
    *ids, = gindex(l, r)
    propagates(*ids)
 
    L = N0 + l; R = N0 + r
    v = x
    while L < R:
        if R & 1:
            R -= 1
            lazy[R-1] = data[R-1] = v
        if L & 1:
            lazy[L-1] = data[L-1] = v
            L += 1
        L >>= 1; R >>= 1; v <<= 1
    for i in ids:
        data[i-1] = data[2*i-1] + data[2*i]
 
# 区間[l, r)内の合計を求める
def query(l, r):
    propagates(*gindex(l, r))
    L = N0 + l; R = N0 + r
 
    s = 0
    while L < R:
        if R & 1:
            R -= 1
            s += data[R-1]
        if L & 1:
            s += data[L-1]
            L += 1
        L >>= 1; R >>= 1
    return s

#普通のセグメント木


# N: 処理する区間の長さ
N0 = 2**(N-1).bit_length()
INF = 2**31-1
data = [INF]*(2*N0)
# a_k の値を x に更新
def update(k, x):
    k += N0-1
    data[k] = x
    while k >= 0:
        k = (k - 1) // 2
        data[k] = min(data[2*k+1], data[2*k+2])
# 区間[l, r)の最小値
def query(l, r):
    L = l + N0; R = r + N0
    s = INF
    while L < R:
        if R & 1:
            R -= 1
            s = min(s, data[R-1])

        if L & 1:
            s = min(s, data[L-1])
            L += 1
        L >>= 1; R >>= 1
    return s