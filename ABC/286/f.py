def egcd(a, b):
	if a == 0:
		return b, 0, 1
	else:
		g, y, x = egcd(b % a, a)
		return g, x - (b // a) * y, y
# https://qiita.com/drken/items/ae02240cd1f8edfc86fd
# a = b1 (mod m1)
# a = b2 (mod m2)
# となるような、 a = r (mod m) を返す
# m=-1のとき解なし。
def crt(bList, mList):
	r, m = 0, 1
	for i in range(len(bList)):
		d, x, y = egcd(m, mList[i])
		if (bList[i] - r) % d != 0:
			return [0, -1]
		tmp = (bList[i] - r) // d * x % (mList[i] // d)
		r += m * tmp
		m *= mList[i] // d
	return [r, m]
print(108)
a=[]
count=2
num=[4,5,7,9,11,13,17,19,23]
num2=[0]
for i in range(9):
	num2.append(num2[-1]+num[i])
for i in num:
	for j in range(i):
		if j==i-1:
			a.append(count-i)
		else:
			a.append(count)
		count+=1
print(" ".join(list(map(str,a))))
x=list(map(int,input().split()))
# x=a
count=0
t=0
ans=1
r=[]
for i in range(9):
	tt=(3*num[i]+x[count]-2-num2[i])%num[i]
	r.append(tt)
	#print(f"{tt} {count}")
	count+=num[i]
print(crt(r, num)[0]+1)
# print(a)
# print(num2)
