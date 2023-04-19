from heapq import *
import sys
input=sys.stdin.readline

def dijkstra(edges, num_node):
    node = [num_node+1] * num_node    #スタート地点以外の値は∞で初期化
    node[0] = 0     #スタートは0で初期化

    node_name = []
    heappush(node_name, [0, 0])

    while len(node_name) > 0:
        #ヒープから取り出し
        cc, min_point = heappop(node_name)
        if node[min_point]<cc:
            continue

        #経路の要素を各変数に格納することで，視覚的に見やすくする
        for factor in edges[min_point]:
            goal ,cost= factor

            #更新条件
            if node[min_point] + cost < node[goal]:
                node[goal] = node[min_point] + cost     #更新
                #ヒープに登録
                heappush(node_name, [node[min_point] + cost, goal])

    return node
n,m=map(int,input().split())
g=[[] for i in range(n+1)]
for i in range(n):
    g[i].append((i+1,1))
    g[i+1].append((i,0))
for i in range(m):
    l,r,x=map(int,input().split())
    g[l-1].append((r,r-l+1-x))
ans=dijkstra(g,n+1)
aa=[str(1-ans[i+1]+ans[i]) for i in range(n)]
print(' '.join(aa))