n=int(input())
s=list(input())
x="atcoder"
p=list(x)
ans=0
l=[0 for i in range(n)]
for i in range(n):
  if s[i]=='a':
    l[i]=1
for i in range(1,7):
  d=0
  for j in range(n):
    if s[j]==x[i-1]:
      d+=l[j]
    if s[j]==x[i]:
      l[j]=d
for i in range(n):
  if s[i]=='r':
    ans+=l[i]
print(ans%1000000007)