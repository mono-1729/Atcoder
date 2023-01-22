def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y
# https://qiita.com/drken/items/ae02240cd1f8edfc86fd
# a = b1 (mod m1)
# a = b2 (mod m2)
# となるような、 a = r (mod m) を返す
# m=-1のとき解なし。
def crt(bList, mList):
    r, m = 0, 1
    for i in range(len(bList)):
        d, x, y = egcd(m, mList[i])
        if (bList[i] - r) % d != 0:
            return [0, -1]
        tmp = (bList[i] - r) // d * x % (mList[i] // d)
        r += m * tmp
        m *= mList[i] // d
    return [r, m]

for _ in range(int(input())):
    n,s,k = map(int, input().split())
    r, m = crt([0, n-s], [k, n])
    if m == -1:
        print(-1)
    else:
        print(r // k)