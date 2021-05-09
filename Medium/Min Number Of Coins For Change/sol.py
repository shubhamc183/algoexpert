# T.C: O(n*denoms) + sorting of denoms 
# S.C : O(n * m)
def minNumberOfCoinsForChange1(n, denoms):
    if n == 0:
        return 0
    denoms.sort()
    denoms_len = len(denoms)
    dp = [[0 for _ in range(n + 1)] for _ in range(denoms_len + 1)]
    for i in range(1 , denoms_len + 1):
        for j in range(1, n + 1):
            if j < denoms[i-1]:
                dp[i][j] = dp[i-1][j]
		continue
            _min = float("inf")
            for d in denoms[0:i]:
                if d > j:
                    break
                elif d == j:
                    _min = 1
                elif dp[i][j-d] > 0:
                    _min = min(1 + dp[i][j-d], _min)
            if _min == float("inf"):
                dp[i][j] = 0
            else:
                dp[i][j] = _min
    return dp[denoms_len][n] if dp[denoms_len][n] > 0 else -1


# T.C: O(n*d) + sorting of denoms 
# S.C : O(n)
def minNumberOfCoinsForChange2(n, denoms):
    if n == 0:
        return 0
    denoms.sort()
    denoms_len = len(denoms)
    coins = [0] * (n + 1)
    for i in range(1, n + 1):
        _min = float("inf")
        for d in denoms:			
            if d > i:
                break
            elif d == i:
                _min = 1
            elif coins[i - d] > 0:
                _min = min(_min, 1 + coins[i-d])
        coins[i] = 0 if _min == float("inf") else _min
    return coins[n] if coins[n] > 0 else -1


# Cleaner Solution
# T.C: O(n*d)
# S.C : O(n)
def minNumberOfCoinsForChange(n, denoms):
    coins = [float("inf")] * (n+1)
    coins[0] = 0
    for i in range(1, n + 1):
        for coin in denoms:
            if i >= coin:
                coins[i] = min(1 + coins[i - coin], coins[i])
    return coins[n] if coins[n] != float("inf") else -1

