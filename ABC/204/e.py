import heapq
n,m=map(int,input().split())
edges=[[] for _ in range(n)]
for i in range(m):
    a,b,c,d=map(int,input().split())
    edges[a-1].append((b-1,c,d))
    edges[b-1].append((a-1,c,d))
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
			d=factor[2]
			min_t=int(max(d**0.5-node[min_point]-1,0))
			min_cost=min(d//(min_t+node[min_point]+1)+min_t,d//(min_t+node[min_point]+2)+min_t+1)
			#更新条件
			if node[min_point] + cost +min_cost < node[goal]:
				node[goal] = node[min_point] + cost +min_cost    #更新
				#ヒープに登録
				heapq.heappush(node_name, [node[min_point] + cost+min_cost, goal])

	return node
node=dijkstra(edges,n)
print(node[n-1] if node[n-1]!=float("inf") else -1)