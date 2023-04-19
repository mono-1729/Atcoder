
"""
2021/01/29
@Yuya Shimizu

ダイクストラ法（ヒープによる優先度付きキューを用いて）
経路を記録する
"""
import heapq

def dijkstra(edges, num_node, Goal):
    """ 経路の表現
            [終点, 辺の値]
            A, B, C, D, ... → 0, 1, 2, ...とする """
    node = [float('inf')] * num_node    #スタート地点以外の値は∞で初期化
    node[0] = 0     #スタートは0で初期化

    node_name = []
    heapq.heappush(node_name, [0, [0]])

    while len(node_name) > 0:
        #ヒープから取り出し
        cc, min_point = heapq.heappop(node_name)
        last = min_point[-1]
        if last == Goal:
            return min_point, node  #道順とコストを出力させている
        if node[min_point[-1]]<cc:
            continue
        #経路の要素を各変数に格納することで，視覚的に見やすくする
        for factor in edges[last]:
            goal = factor[0]   #終点
            cost  = factor[1]   #コスト

            #更新条件
            if node[last] + cost < node[goal]:
                node[goal] = node[last] + cost     #更新
                #ヒープに登録
                heapq.heappush(node_name, [node[last] + cost, min_point + [goal]])

    return []

if __name__ == '__main__':
    Edges = [
        [[1, 4], [2, 3]],             # ← 頂点Aからの辺のリスト
        [[2, 1], [3, 1], [4, 5]],   # ← 頂点Bからの辺のリスト
        [[5, 2]],                       # ← 頂点Cからの辺のリスト
        [[4, 3]],                       # ← 頂点Dからの辺のリスト
        [[6, 2]],                       # ← 頂点Eからの辺のリスト
        [[4, 1], [6, 4]],             # ← 頂点Fからの辺のリスト
        []                                # ← 頂点Gからの辺のリスト
        ]

    #今の目的地の数は7つ（0~6: A~G）
    node_num = 7
    Goal = 6    
    opt_root, opt_cost = dijkstra(Edges, node_num, Goal)    #道順とコストを出力させている

    #出力を見やすく整理するための変換用辞書型リストの作成
    root_converter = {}
    cost_converter = {}
    for i in range(node_num):
        root_converter[i] = chr(ord('A') + i)
        cost_converter[i] = opt_cost[i]

    arrow = " → "
    result = ""
    for i in range(len(opt_root)):
        if i > 0:
            result += arrow
        result += f"{root_converter[opt_root[i]]}({cost_converter[opt_root[i]]})"

    print(f"ノード(そこまでのコスト)\n\n{result}")

"""
2021/01/29
@Yuya Shimizu

ダイクストラ法（ヒープによる優先度付きキューを用いて）
"""
import heapq

def dijkstra(edges, num_node):
    """ 経路の表現
            [終点, 辺の値]
            A, B, C, D, ... → 0, 1, 2, ...とする """
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

if __name__ == '__main__':
    Edges = [
        [[1, 4], [2, 3]],             # ← 頂点Aからの辺のリスト
        [[2, 1], [3, 1], [4, 5]],   # ← 頂点Bからの辺のリスト
        [[5, 2]],                       # ← 頂点Cからの辺のリスト
        [[4, 3]],                       # ← 頂点Dからの辺のリスト
        [[6, 2]],                       # ← 頂点Eからの辺のリスト
        [[4, 1], [6, 4]],             # ← 頂点Fからの辺のリスト
        []                                # ← 頂点Gからの辺のリスト
        ]

    #今の目的地の数は7つ（0~6: A~G）
    node_num = 7

    opt_node = dijkstra(Edges, node_num)

    #以下は結果を整理するためのコード
    node_name = []
    for i in range(node_num):
        node_name.append(chr(ord('A') + i))    
    result = []
    for i in range(len(opt_node)):
        result.append(f"{node_name[i]} : {opt_node[i]}")
    print(f"'目的地:そこまでの最小コスト'\n\n{result}")