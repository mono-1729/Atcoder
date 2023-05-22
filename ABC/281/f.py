n=int(input())
a=set(map(int,input().split()))
exp=[1<<i for i in range(30)]
def solve(s,digit):
  if digit==-1:
      return 0
  ones=set()
  zeros=set()
  for i in s:
      if i&exp[digit]:
          ones.add(i)
      else:
          zeros.add(i)
  if len(ones)==0 or len(zeros)==0:
      return solve(s,digit-1)
  else:
      return exp[digit]+min(solve(ones,digit-1),solve(zeros,digit-1))
print(solve(a,29))