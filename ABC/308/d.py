from collections import deque
h,w=map(int,input().split())
s=[list(input()) for i in range(h)]
can=[[0]*w for i in range(h)]
snuke={}
ward='snuke'
for i in range(5):
    snuke[ward[i]]=ward[(i+1)%5]
que = deque()
if s[0][0] in ward:
    can[0][0]=1
    que.append((0,0))
 
while len(que) > 0:
    i, j = que.popleft()

    # 4方向の遷移
    for i2, j2 in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
        if not (0 <= i2 < h and 0 <= j2 < w):
            continue
        # この経路での始点から遷移先までの距離。壁なら+1
        if s[i2][j2]!=snuke[s[i][j]]:
            continue
        if can[i2][j2]==0:
            can[i2][j2]=1
            que.append((i2, j2))
if can[h-1][w-1]:
    print('Yes')
else:
    print('No')
