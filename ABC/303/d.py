from functools import lru_cache
import sys
sys.setrecursionlimit(8*10**5)
x,y,z=map(int,input().split())
s=list(input())
@lru_cache(maxsize=None)
def main(i,lock):
	if i==len(s):
		return 0
	if lock==1:
		if s[i]=='a':
			return min(main(i+1,1)+y,main(i+1,0)+x+z)
		else:
			return min(main(i+1,1)+x,main(i+1,0)+y+z)
	else:
		if s[i]=='A':
			return min(main(i+1,0)+y,main(i+1,1)+x+z)
		else:
			return min(main(i+1,0)+x,main(i+1,1)+y+z)
print(main(0,0))