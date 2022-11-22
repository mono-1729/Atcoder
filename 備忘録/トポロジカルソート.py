#グラフでDFSを実行し、すべての出発時刻を設定します
# グラフの#頂点
def DFS(graph, v, discovered, departure, time):
 
    #は、現在のノードを検出済みとしてマークします
    discovered[v] = True
 
    #は頂点`v`の到着時間を設定します
    time = time + 1
 
    #はすべてのエッジに対して実行します(v、u)
    for u in graph[v]:
        # `u`がまだ発見されていない場合は
        if not discovered[u]:
            time = DFS(graph, u, discovered, departure, time)
 
    #はバックトラックする準備ができています
    #は頂点`v`の出発時刻を設定しました
    departure[time] = v
    time = time + 1
 
    return time
 
 
#特定のDAGでトポロジカルソートを実行する関数
def doTopologicalSort(graph, n):
 
    # departure[]は、出発時刻をインデックスとして使用して頂点番号を格納します
    departure = [-1] * 2 * n
 
    ''' If we had done it the other way around, i.e., fill the array
        with departure time using vertex number as an index, we would
        need to sort it later '''
 
    # 頂点が検出されたかどうかを追跡する
    discovered = [False] * n
    time = 0
 
    #は、検出されていないすべての頂点でDFSを実行します
    for i in range(n):
        if not discovered[i]:
            time = DFS(graph, i, discovered, departure, time)
 
    #頂点を降順で印刷します
    # DFSでの#出発時間、つまりトポロジカル順
    for i in reversed(range(2*n)):
        if departure[i] != -1:
            print(departure[i], end=' ')