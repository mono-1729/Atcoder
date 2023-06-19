import heapq
n,m,k=map(int,input().split())
node=[1]*n
edges=[[] for _ in range(n)]
node_name = []
for i in range(m):
    a,b=map(int,input().split())
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)
for i in range(k):
    p,h=map(int,input().split())
    node[p-1]=-h
    heapq.heappush(node_name, (-h,p-1))
    
while len(node_name) > 0:
	#ヒープから取り出し
	cc, min_point = heapq.heappop(node_name)
	if cc>0:
		break
	if node[min_point]<cc:
		continue
	#経路の要素を各変数に格納することで，視覚的に見やすくする
	for factor in edges[min_point]:
		if node[min_point] + 1 < node[factor]:
			node[factor] = node[min_point] + 1    #更新
			#ヒープに登録
			heapq.heappush(node_name, (node[min_point] + 1, factor))
ans=[]
for i in range(n):
	if node[i]<=0:
		ans.append(i+1)
print(len(ans))
print(*ans)
