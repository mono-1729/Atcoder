n=int(input())
a=list(input())
b=list(input())
for i in range(n):
    if int(a[i])>int(b[i]):
        tmp=a[i]
        a[i]=b[i]
        b[i]=tmp
print((int(''.join(a))*int(''.join(b)))%998244353)
