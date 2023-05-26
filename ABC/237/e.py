import heapq

def dijkstra(edges, num_node):
    node = [float('inf')] * num_node    #スタート地点以外の値は∞で初期化
    node[0] = 0     #スタートは0で初期化

    node_name = []
    heapq.heappush(node_name, [0, 0])

    while len(node_name) > 0:
        #ヒープから取り出し
        cc, min_point = heapq.heappop(node_name)
        if node[min_point]<cc:
            continue
        #経路の要素を各変数に格納することで，視覚的に見やすくする
        for factor in edges[min_point]:
            goal = factor[0]   #終点
            cost  = factor[1]   #コスト

            #更新条件
            if node[min_point] + cost < node[goal]:
                node[goal] = node[min_point] + cost     #更新
                #ヒープに登録
                heapq.heappush(node_name, [node[min_point] + cost, goal])

    return node
n,m=map(int,input().split())
h=list(map(int,input().split()))
edges=[[] for i in range(n)]
for i in range(m):
    u,v=map(int,input().split())
    u,v=u-1,v-1
    if h[u]>=h[v]:
        edges[u].append([v,0])
        edges[v].append([u,-h[v]+h[u]])
    else:
        edges[u].append([v,-h[u]+h[v]])
        edges[v].append([u,0])
dist=dijkstra(edges,n)
ans=0
for i in range(n):
    ans=max(ans,h[0]-h[i]-dist[i])
print(ans)
