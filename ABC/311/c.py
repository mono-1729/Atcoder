from collections import deque
import sys
sys.setrecursionlimit(3*10**5)
if "pypyjit" in sys.builtin_module_names:
	import pypyjit
	pypyjit.set_param("max_unroll_recursion=-1")

n=int(input())
seen=[False]*n
g=[0 for i in range(n)]
a=list(map(int,input().split()))
for i in range(n):
	g[i]=a[i]-1

path=[0]
seen=[False]*n
while True:
	seen[path[-1]]=True
	path.append(g[path[-1]])
	if seen[path[-1]]:
		break
ans=[]
flg=False
for i in range(len(path)-1):
	if path[i]==path[-1]:
		flg=True
	if flg:
		ans.append(path[i]+1)
#print(path)
print(len(ans))
print(' '.join(map(str,ans)))