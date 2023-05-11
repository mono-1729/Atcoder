w=int(input())
print(300)
ans=[]
for i in range(3):
    for j in range(1,101):
    	ans.append(str((100**i)*j))
print(' '.join(ans))
