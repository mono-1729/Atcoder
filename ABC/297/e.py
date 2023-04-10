import heapq
n,k=map(int,input().split())
a=list(map(int,input().split()))
node = set() 
node_name = []
count=0
heapq.heappush(node_name,0)

while len(node_name) > 0 and len(node)<=k*10:
	#ヒープから取り出し
	num = heapq.heappop(node_name)
	for tako in a:
		if not (num+tako in node):
			node.add(num+tako)
			heapq.heappush(node_name,num+tako)
money=list(node)
money.sort()
print(money[k-1])
