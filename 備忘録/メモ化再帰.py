from functools import lru_cache
from functools import lru_cache
import sys
sys.setrecursionlimit(3*10**5)
if "pypyjit" in sys.builtin_module_names:
	import pypyjit
	pypyjit.set_param("max_unroll_recursion=-1")

@lru_cache(maxsize=None)
def hoge(n):
	pass