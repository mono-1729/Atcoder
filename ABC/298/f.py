n=int(input())
rcx=[]
rc=set()
for i in range(n):
    r,c,x=map(int,input().split())
    rc.add(r)
    rc.add(c)
    rcx.append([r,c,x])
rc=list(rc)
rc.sort()
cr={}
ver=[[0,i] for i in range(len(rc))]
hol=[[0,i] for i in range(len(rc))]
exist={}
for i,m in enumerate(rc):
    cr[m]=i
for i in range(n):
    r,c,x=rcx[i]
    exist[f"{cr[r]},{cr[c]}"]=x
    ver[cr[r]][0]+=x
    hol[cr[c]][0]+=x
ans=0
ver.sort(reverse=True)
hol.sort(reverse=True)
for i in range(len(ver)):
    num=0
    if ans>ver[i][0]+hol[0][0]:
        break
    for j in range(len(hol)):
        if num>ver[i][0]+hol[j][0]:
            break
        if f"{ver[i][1]},{hol[j][1]}" in exist:
            point=ver[i][0]+hol[j][0]-exist[f"{ver[i][1]},{hol[j][1]}"]
            num=max(num,point)
            ans=max(ans,point)
        else:
            ans=max(ans,ver[i][0]+hol[j][0])
            break
print(ans)

