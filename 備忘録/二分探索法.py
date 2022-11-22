n,l=map(int,input().split())
k=int(input())
a=list(map(int,input().split()))
def is_ok(arg):
  cnt = 0
  pre = 0
  for i in range(n):
    if a[i] - pre >= arg:
      cnt += 1
      pre = a[i]
  if l - pre >= arg:
    cnt+=1
  return(cnt>=k+1)
def meguru_bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2 
        if is_ok(mid):
            ng = mid
        else:
            ok = mid
    return ng
print(meguru_bisect(-1,l+1))

def binary_search(data, value):
    left = 0            # 探索する範囲の左端を設定
    right = len(data) - 1            # 探索する範囲の右端を設定
    while left <= right:
        mid = (left + right) // 2            # 探索する範囲の中央を計算
        if data[mid] == value:
            # 中央の値と一致した場合は位置を返す
            return mid
        elif data[mid] < value:
            # 中央の値より大きい場合は探索範囲の左を変える
            left = mid + 1
        else:
            # 中央の値より小さい場合は探索範囲の右を変える
            right = mid - 1
    return -1            # 見つからなかった場合

data = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(binary_search(data, 90))




#簡単な二分探索
