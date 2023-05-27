from functools import lru_cache
import sys
sys.setrecursionlimit(3*10**5)
if "pypyjit" in sys.builtin_module_names:
	import pypyjit
	pypyjit.set_param("max_unroll_recursion=-1")
n=int(input())
s=list(input())
x=list(input())
@lru_cache(maxsize=None)
def main(i,mod):
	if i==n:
		if mod==0:
			return 1
		else:
			return 0
	if x[i]=='T':
		return main(i+1,mod) or main(i+1,(mod+int(s[i])*pow(10,n-i-1,7))%7)
	else:
		return main(i+1,mod) and main(i+1,(mod+int(s[i])*pow(10,n-i-1,7))%7)
if main(0,0):
	print('Takahashi')
else:
	print('Aoki')
