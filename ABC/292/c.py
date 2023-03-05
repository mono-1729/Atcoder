n=int(input())
def getNumsOfDivisorsOfEachNumbers(n: int):
    # validation check
    if not isinstance(n, int):
        raise("[ERROR] parameter must be integer")
    if n < 0:
        raise("[ERROR] parameter must be not less than 0 (n >= 0)")
    nums = [0] * (n + 1) # 0-indexed
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            nums[j] += 1
    nums.pop(0)
    return nums
ans=0
nums=getNumsOfDivisorsOfEachNumbers(n)

for i in range(1,n):
    ans+=nums[i-1]*nums[n-i-1]
print(ans)