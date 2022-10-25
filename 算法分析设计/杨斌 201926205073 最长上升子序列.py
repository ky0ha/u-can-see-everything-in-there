def lis(array:list):
    dp = [0 for _ in range(len(array))]
    dp[0] = 1
    result = 1
    for i in range(len(array)):
        _max = 1
        dp[i] = 1
        for j in range(i):
            if array[i] > array[j]:
                dp[i] = dp[j] + 1
            if _max < dp[i]:
                _max = dp[i]
        dp[i] = _max
        if result < dp[i]:
            result = dp[i]
    print(dp)
    return result

ls = [8, 12, 2, 7, 6, 9]
print(lis(ls))