from bisect import bisect_right
def prime_factor_table(n):
    table = [0] * (n + 1)
    
    for i in range(2, n + 1):
        if table[i] == 0:
            for j in range(i + i, n + 1, i):
                table[j] = i
    
    return table
n=int(input())
prime=prime_factor_table(10**6)
p=[]
ans=0
for i in range(2,10**6):
    if prime[i]==0:
        p.append(i)
for i in range(60):
    for j in range(i+1,1300):
        if p[i]*p[i]*p[j]*p[j+1]*p[j+1]<=n:
            ans+=bisect_right(p,(n//(p[i]*p[i]*p[j]))**0.5)-j-1
print(ans)
