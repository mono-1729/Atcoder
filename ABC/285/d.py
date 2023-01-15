from collections import defaultdict
import sys
sys.setrecursionlimit(3*10**5)
if "pypyjit" in sys.builtin_module_names:
	import pypyjit
	pypyjit.set_param("max_unroll_recursion=-1")
n=int(input())
sdict=defaultdict(int)
st=[]
stdict=dict()
for i in range(n):
	s,t=input().split()
	st.append([s,t])
	sdict[s]=i+1
	stdict[s]=t
seen=[0]*n
def dfs(G, v,k):
	global seen
	tt=stdict[G]
	next_v= sdict[tt]-1
	if next_v!=-1:
		if next_v==k:
			print('No')
			exit()
		seen[v]=1
		#print(f'{G} {v} {next_v} {tt} {seen}')
		dfs(tt, next_v,k)
	seen[v]=1
for i in range(n):
	if seen[i]==0:
		dfs(st[i][0],i,i)
print('Yes')