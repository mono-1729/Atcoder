x,y,a,b,c=map(int,input().split())
s='No'
if (a-1)//x+(b-1)//x+(c-1)//x+3<=y:
    s='Yes'
if (a-1)//y+(b-1)//y+(c-1)//y+3<=x:
    s='Yes'
l=[a,b,c]
for i in range(3):
    xx=(l[i]-1)//y+1
    if x-xx>0 and (l[(i+1)%3]-1)//(x-xx)+(l[(i+2)%3]-1)//(x-xx)+2<=y:
        s='Yes'
    yy=(l[i]-1)//x+1
    if y-yy>0 and (l[(i+1)%3]-1)//(y-yy)+(l[(i+2)%3]-1)//(y-yy)+2<=x:
        s='Yes'
print(s)