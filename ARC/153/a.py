n=str(int(input())-1)
a=['0']*6
for i in reversed(range(len(n))):
	a[i+6-len(n)]=n[i]
l=[]
l.append(str(int(a[0])+1))
l.append(str(int(a[0])+1))
l.append(str(int(a[1])))
l.append(str(int(a[2])))
l.append(str(int(a[3])))
l.append(str(int(a[3])))
l.append(str(int(a[4])))
l.append(str(int(a[5])))
l.append(str(int(a[4])))
print(''.join(l))