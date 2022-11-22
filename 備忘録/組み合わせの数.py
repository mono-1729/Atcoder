n=int(input())
a=[1,1]
b=[]
for i in range(2,n+2):
  a.append(a[i-1]*i%1000000007)#階乗を求める
for i in range(n+1):
  b.append(pow(a[i],1000000005,1000000007))#1/a[i]の逆元を計算(x/a[i]とかの場合前にxを掛ける)
for i in range(1,n+1):
  ans=0
  for j in range(1,n//i+2):
    if n-(i-1)*(j-1)>=j:
      ans+=a[n-(i-1)*(j-1)]*b[j]%1000000007*b[n-(i-1)*(j-1)-j]%1000000007
  print(ans%1000000007)
    