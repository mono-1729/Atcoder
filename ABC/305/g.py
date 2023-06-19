n,m=map(int,input().split())
slist=set([input() for _ in range(m)])
if n<6:
	ans=0
	for i in range(2**n):
		s=''
		flg=True
		for j in range(n):
			if i>>j&1:
				s+='a'
			else:
				s+='b'
		for i in range(n):
			for j in range(i+1,n+1):
				if s[i:j] in slist:
					flg=False
					break
		if flg:
			ans+=1
	print(ans)
else:
	ans=0
	ablist=[]
	for i in range(2**6):
		s=''
		flg=True
		for j in range(6):
			if i>>j&1:
				s+='a'
			else:
				s+='b'
		for i in range(6):
			for j in range(i+1,6+1):
				if s[i:j] in slist:
					flg=False
					break
		if flg:
			ablist.append(s)
	abset=set(ablist)
	num=[0]*(len(ablist))
	num2=[0]*(len(ablist))
	for x in range(len(ablist)):
		for tt in ablist:
			ss=ablist[x]
			flg=True
			sstt=ss+tt
			for i in range(1,6):
				if sstt[i:i+6] not in abset:
					flg=False
					break
			if flg:
				num[x]+=1
	dd=n%6
	nablist=[]
	for i in range(2**dd):
		s=''
		flg=True
		for j in range(dd):
			if i>>j&1:
				s+='a'
			else:
				s+='b'
		for i in range(dd):
			for j in range(i+1,dd+1):
				if s[i:j] in slist:
					flg=False
					break
		if flg:
			nablist.append(s)
	for x in range(len(ablist)):
		for tt in ablist:
			ss=ablist[x]
			flg=True
			sstt=ss+tt
			for i in range(1,6):
				if sstt[i:i+6] not in abset:
					flg=False
					break
			if flg:
				num[x]+=1

	print(ans)