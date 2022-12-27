u'''
2部グラフの判定を行うプログラム

N := 頂点の数
M := 辺の数

A,B := 頂点Aから頂点Bにかけて無向の辺があることを示す

dict := 辺のつながりを格納する
     collections の dict だとValueに配列を格納しやすい

color:= 頂点が何色で塗られているか

'''
from collections import defaultdict 

N ,M= map(int,input().split())
dict = defaultdict(set)

for i in range(M):
    a,b = list(map(int,input().split()))  

    dict[a].add(b)
    dict[b].add(a)



color = [0 for i in range(N+1)]
res = 'Yes'

def dfs(v,c,queue=[]):
    u'''
    v : 現在のグラフの頂点
    c : 現在参照するフラグ,1=>-1=>1と使うので渡す必要がある
    queue : 探索したグラフの頂点を入れていく
    res : global変数を使いたくないが,再帰のreturnがよくわからないのでとりあえず
    '''

    global color
    global res 
    queue.append(v)

    for i in list(dict[v]):
        if color[i] == c:#隣の頂点が同じ値を与えられている際Falseを返す
            res = 'No'
        elif i not in queue:#探索済みでなければ再帰する
            color[i] = c*-1#0ならcとは異なる値を格納
            dfs(i,-c,queue)#引数に-cとすることで,cが1=>-1=>1を繰り返す


color[1] = 1#始点色分けする
(dfs(1,1))
print(res)

#パターン2
from collections import deque
from collections import defaultdict

N,M = list(map(int,input().split()))
G = defaultdict(set)

color = [0 for i in range(N+1)]

for _ in range(M):
    A,B = map(int,input().split())
    G[A].add(B)
    G[B].add(A)

color[1] = 1
que = deque([1])#始点を追加
bipartite = True

while len(que):
    p = que.popleft()#直近で追加したグラフの頂点を取得
    for q in list(G[p]):#結合しているグラフの頂点を参照
        if color[q] == 0:#塗られていないなら別の色で塗る
            color[q] = -color[p]
            que.append(q)
        elif color[q] == color[p]:#同じ色だったら2部グラフではないと返し終了させる
            bipartite = False
            break